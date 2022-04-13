#!/usr/bin/env python
# -*- coding: utf-8 -*-

####################################################################
# 프로그램명 : hough_drive.py
# 작 성 자 : 자이트론
# 생 성 일 : 2020년 08월 12일
# 수 정 일 : 2021년 03월 16일
# 검 수 인 : 조 이현
# 본 프로그램은 상업 라이센스에 의해 제공되므로 무단 배포 및 상업적 이용을 금합니다.
####################################################################

import rospy, rospkg
import numpy as np
import cv2, random, math
from cv_bridge import CvBridge
from xycar_msgs.msg import xycar_motor
from sensor_msgs.msg import Image

from movingAverage import MovingAverage
from pid_control import PID

import sys
import os
import signal
import time

def signal_handler(sig, frame):
    os.system('killall -9 python rosout')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

image = np.empty(shape=[0])
bridge = CvBridge()
pub = None
Width = 640
Height = 480
Offset = 370
Gap = 40


def img_callback(data):
    global image    
    image = bridge.imgmsg_to_cv2(data, "bgr8")


# publish xycar_motor msg
def drive(Angle, Speed): 
    global pub

    msg = xycar_motor()
    msg.angle = Angle
    msg.speed = Speed

    pub.publish(msg)


# draw lines
def draw_lines(img, lines):
    global Offset
    for line in lines:
        x1, y1, x2, y2 = line[0]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        img = cv2.line(img, (x1, y1+Offset), (x2, y2+Offset), color, 2)
    return img


# draw rectangle
def draw_rectangle(img, lpos, rpos, offset=0):
    center = (lpos + rpos) / 2

    cv2.rectangle(img, (lpos - 5, 15 + offset),
                       (lpos + 5, 25 + offset),
                       (0, 255, 0), 2)
    cv2.rectangle(img, (rpos - 5, 15 + offset),
                       (rpos + 5, 25 + offset),
                       (0, 255, 0), 2)
    cv2.rectangle(img, (center-5, 15 + offset),
                       (center+5, 25 + offset),
                       (0, 255, 0), 2)    
    cv2.rectangle(img, (315, 15 + offset),
                       (325, 25 + offset),
                       (0, 0, 255), 2)
    return img


# left lines, right lines
def divide_left_right(lines):
    global Width
    low_slope_threshold = 0
    high_slope_threshold = 10

    slopes = []
    new_lines = []

    for line in lines:
        x1, y1, x2, y2 = line[0]
        if x2 - x1 == 0:
            slope = 0
        else:
            slope = float(y2 - y1) / float(x2 - x1)
        if (abs(slope) > low_slope_threshold) and (abs(slope) < high_slope_threshold):
            slopes.append(slope)
            new_lines.append(line[0])
    
    # divide lines left to right
    left_lines = []
    right_lines = []
    left_x_sum = 0
    right_x_sum = 0

    for j in range(len(slopes)):
        Line = new_lines[j]
        slope = slopes[j]
        x1, y1, x2, y2 = Line
        if slope < 0:
            left_lines.append([Line.tolist()])
            left_x_sum += (x1 + x2)/2
        else:
            right_lines.append([Line.tolist()])
            right_x_sum += (x1 + x2)/2

    if len(left_lines) != 0 and len(right_lines) != 0:
        left_x_avg = left_x_sum / len(left_lines)
        right_x_avg = right_x_sum / len(right_lines)

        if left_x_avg > right_x_avg:
            left_lines = []
            right_lines = []

    return left_lines, right_lines


# get average m, b of lines
def get_line_params(lines):
    # sum of x, y, m
    x_sum = 0.0
    y_sum = 0.0
    m_sum = 0.0

    size = len(lines)
    if size == 0:
        return 0, 0

    for line in lines:
        x1, y1, x2, y2 = line[0]

        x_sum += x1 + x2
        y_sum += y1 + y2
        m_sum += float(y2 - y1) / float(x2 - x1)

    x_avg = x_sum / (size * 2)
    y_avg = y_sum / (size * 2)
    m = m_sum / size
    b = y_avg - m * x_avg

    return m, b


# get lpos, rpos
def get_line_pos(img, lines, left=False, right=False):
    global Width, Height
    global Offset, Gap

    m, b = get_line_params(lines)

    if m == 0 and b == 0:
        if left:
            pos = 0
        if right:
            pos = Width
    else:
        y = Gap / 2
        pos = (y - b) / m

        b += Offset
        x1 = (Height - b) / float(m)
        x2 = ((Height/2) - b) / float(m)

        cv2.line(img, (int(x1), Height), (int(x2), (Height/2)), (255, 0,0), 3)

    return img, int(pos), m


# show image and return lpos, rpos
def process_image(frame):
    global Width
    global Offset, Gap

    # gray
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # blur
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

    # canny edge
    low_threshold = 150
    high_threshold = 200

    edge_img = cv2.Canny(np.uint8(blur_gray), low_threshold, high_threshold)
    #cv2.imshow('edge_img', edge_img)

    # HoughLinesP
    roi = edge_img[Offset : Offset+Gap, 0 : Width]
    #cv2.imshow('roi', roi)

    all_lines = cv2.HoughLinesP(roi,1,math.pi/180,40,35,10)

    # divide left, right lines
    if all_lines is None:
        #cv2.imshow('calibration', frame)
        return 0, 640, 0, 0
    left_lines, right_lines = divide_left_right(all_lines)

    # get center of lines
    frame, lpos, l_slope = get_line_pos(frame, left_lines, left=True)
    frame, rpos, r_slope = get_line_pos(frame, right_lines, right=True)

    # draw lines
    frame = draw_lines(frame, left_lines)
    frame = draw_lines(frame, right_lines)
    frame = cv2.line(frame, (230, 235), (410, 235), (255,255,255), 2)
                                 
    # draw rectangle
    frame = draw_rectangle(frame, lpos, rpos, offset=Offset)

    # show image
    #cv2.imshow('calibration', frame)

    return lpos, rpos, l_slope, r_slope


def get_steer_angle(curr_position, l_slope, r_slope):
    # Lane tracking algorithm here

    k = 1.0

    if -0.2 < curr_position < 0.2 :  # 좀 더 천천히 조향해도 괜찮은 상황
        k = 1.0
    
    elif curr_position > 0.4 or curr_position < -0.4 :  # 신속하게 가운데로 들어와야 함
        k = 4.0

    else:   # 그 중간의 경우 계수는 linear 변화
        k = 20.0 * abs(curr_position) - 3.0

    steer_angle = k * math.atan(curr_position)* 180 / math.pi

    return steer_angle


def velocity_control(l_slope, r_slope):

    if abs(l_slope) < 0.45 or abs(r_slope) < 0.45:
        speed = 15

    else:
        speed = 50

    return speed


def start():
    global pub
    global image
    global Width, Height
    global prev_angle

    mm1 = MovingAverage(20)
    mm2 = MovingAverage(20)

    prev_angle = 0

    rospy.init_node('auto_drive')
    pub = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)

    image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, img_callback)
    print "---------- Xycar A2 v1.0 ----------"

    while True:
        while not image.size == (640*480*3):
            continue

        lpos, rpos, lslope, rslope = process_image(image)

        position = (float(lpos + rpos - Width)) / Width

        steering_gain = 0.8
        steer_angle = steering_gain * get_steer_angle(position, lslope, rslope)

        if steer_angle == 0:
            steer_angle = prev_angle

        mm1.add_sample(steer_angle)
        wmm_angle = mm1.get_wmm()

        # print("lpos = ", lpos, "rpos = ", rpos, "position = ", position, "angle = ", steer_angle)

        speed = velocity_control(lslope, rslope)
        mm2.add_sample(speed)
        mm_speed = mm2.get_wmm()
        drive(wmm_angle, mm_speed)

        prev_angle = steer_angle

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    rospy.spin()

if __name__ == '__main__':

    start()


