n = int(input())

arr = list(map(int, input().split()))

if n == 1 or n == 2:
    print(n)
    exit(0)

arr.sort()

s = 0
e = 2
max = 2

while e != n:
    if arr[s] + arr[s+1] > arr[e]:
        if max < (e-s+1):
            max = (e-s+1)
            # print("start", s, "end", e)
        e += 1
    else:
        s += 1
        e = s + 2

e -= 1
if arr[s] + arr[s+1] > arr[e]:
    if max < (e-s+1):
        max = (e-s+1)
        # print("start", s, "end", e)

print(max)