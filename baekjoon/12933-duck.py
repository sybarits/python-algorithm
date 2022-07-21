import sys
word = list(sys.stdin.readline().rstrip())

sound = {'q':1, 'u':2, 'a':3, 'c':4, 'k':5}

if len(word) % 5 != 0:
    print(-1)
    exit(0)

max_ducks = len(word)/5
ducks = 0
cnt = 0
while len(word) != 0:
    index = 0
    duck_cnt = 0
    prev_sound = 0
    while index != len(word):
        # print("index", index, "word", word)
        if sound[word[index]] - prev_sound == 1:
            if sound[word[index]] == 5:
                prev_sound = 0
                duck_cnt += 1
            else:
                prev_sound = sound[word[index]]
            del word[index]
        else:
            index += 1
    cnt += 1
    if duck_cnt > 0:
        ducks += 1
    if cnt > max_ducks:
        break

if len(word) != 0 or ducks == 0:
    print(-1)
    exit(0)

print(ducks)