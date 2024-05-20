from calendar import calendar


n = int(input())

calendar = [0 for i in range(366)]
schedule = []

for _ in range(n):
    s,e = map(int, input().split())
    # print(s,e)
    schedule.append([s, e, e-s+1])

# schedule.sort(key=lambda x: (x[0], -x[1]))

result = 0
block_s, block_e, block_h = 0, 0, 0
for i, d in enumerate(schedule):
    for j in range(d[0],d[1]+1):
        calendar[j] += 1

# print("calendar")
# print(calendar)

for i, s in enumerate(calendar):
    if s == 0:
        result += block_h * (block_e - block_s + 1)
        block_s, block_e, block_h = i + 1, i + 1, 0
        # print("i", i, "result", result)
    elif s != 0:
        if block_h < s:
            block_h = s
        block_e = i

result += block_h * (block_e - block_s + 1)

print(result)    

