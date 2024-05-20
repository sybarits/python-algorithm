import sys
from unittest import skip
word = list(sys.stdin.readline().rstrip())

index = 0

while index != len(word):
    if word[index] == '<':
        while word[index] != '>':
            index += 1
        index += 1
    elif word[index].isalnum():
        w = ""
        start = index
        while index < len(word) and word[index].isalnum():
            index += 1
        w = word[start:index]
        w.reverse()
        word[start:index] = w
    else:
        index += 1

print("".join(word))


