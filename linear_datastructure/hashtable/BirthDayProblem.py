# -*- coding: utf-8 -*-
# 23명이 같이 있으면 생일이 같은 사람이 있을 확률이 50%를 넘을까?

import random


if __name__ == "__main__":
    
    TRIALS = 100000
    same_birthdays = 0

    for _ in range(TRIALS):
        birthdays = []
        for i in range(23):
            birthday = random.randint(1,365)
            if birthday in birthdays:
                same_birthdays += 1
                break
            birthdays.append(birthday)
    
    print("result", f"{same_birthdays / TRIALS * 100}%")