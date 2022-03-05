# -*- coding: utf-8 -*-
import math

def solution(n):
    t1 = 1
    t2 = 2

    for i in range(3,n+1):
        t3 = t1 + t2
        t1, t2 = t2, t3

    return t3 % 1000000007


if __name__ == "__main__":
    print(solution(4))#5
    # print(solution(60000))#5


    # print("partial factorial", partial_factorial(4,3))
