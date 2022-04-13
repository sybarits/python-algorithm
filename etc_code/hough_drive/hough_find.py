#!usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import numpy as np
import cv2, random, math, time

Width = 640
Height = 480
Offset = 420
Gap = 40

# draw lines
# 허프변환 함수로 검출된 모든 선분을 알록달록하게 출력
def draw_lines(img, lines):
    global Offset
    for line in lines:
        x1, y1, x2, y2 = line[0]
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        img = cv2.line(img, (x1, y1 + Offset), (x2, y2 + Offset), color, 2)
    return img

# draw rectangle
def draw_rectangle(img, lpos, rpos, offset=0):
    center = (lpos + rpos) / 2
    cv2.rectangle(img, (lpos - 5, 15 + offset), (lpos + 5, 25 + offset), (0, 255, 0), 2)
    cv2.rectangle(img, (rpos - 5, 15 + offset), (rpos + 5, 25 + offset), (0, 255, 0), 2)
    cv2.rectangle(img, (center - 5, 15 + offset), (center + 5, 25 + offset), (0, 255, 0), 2)
    cv2.rectangle(img, (315, 15 + offset), (325, 25 + offset), (0, 0, 255), 2)
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

    for j in range(len(slopes)):
        Line = new_lines[j]
        slope = slopes[j]
        x1, y1, x2, y2 = Line
        if (slope < 0) and (x2 < Width/2 - 90):
            left_lines.append([Line.tolist()])

        elif (slope > 0) and (x1 > Width/2 + 90):
            right_lines.append([Line.tolist()])

    return left_lines, right_lines

# get average m, b of lines
def get_line_params(lines):
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
        x2 = ((Height / 2) - b) / float(m)

        cv2.line(img, (int(x1), Height), (int(x2), (Height / 2)), (255, 0, 0), 3)

    return img, int(pos)

# show image and return lpos, rpos
def process_image(frame):
    global Width
    global Offset, Gap

    # gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # blur
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

    # canny edge
    low_threshold = 60
    high_threshold = 70
    edge_img = cv2.Canny(np.uint8(blur_gray), low_threshold, high_threshold)
    
    # Offset = 420
    # Gap = 40
    # HoughLinesP
    # roi = edge_img[Offset : Offset + Gap, 0 : Width]
    roi = edge_img[Offset : Offset + Gap, 0 : Width]

    all_lines = cv2.HoughLinesP(roi, 1, math.pi/180, 30, 30, 10)

    # divide left, right lines
    if all_lines is None:
        return 0, 640
    left_lines, right_lines = divide_left_right(all_lines)

    # get center of lines
    frame, lpos = get_line_pos(frame, left_lines, left=True)
    frame, rpos = get_line_pos(frame, right_lines, right=True)

    # draw lines
    frame = draw_lines(frame, left_lines)
    frame = draw_lines(frame, right_lines)
    frame = cv2.line(frame, (230, 235), (410, 235), (255, 255, 255), 2)

    # draw rectangle
    frame = draw_rectangle(frame, lpos, rpos, offset=Offset)
    cv2.imshow("dd", frame)

    return lpos, rpos

# draw steer
def draw_steer(image, steer_angle):
    pass

def start():
    global image, Width, Height

    # cap = cv2.VideoCapture('base_camera_dark.avi')
    video = 'xycar_track1.mp4'
    cap = cv2.VideoCapture('base_camera_dark.avi')

    while not rospy.is_shutdown():
        ret, image = cap.read()
        if not ret:
            rospy.sleep(0.1)
            cap = cv2.VideoCapture(video)
            continue
        time.sleep(0.03)

        lpos, rpos = process_image(image)

        center = (lpos + rpos) / 2
        angle = 320 - center
        steer_angle = angle * 0.4

        print("lpos = ", lpos, "rpos = ", rpos, "angle = ", steer_angle)
        # draw_steer(frame, steer_angle)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    start()