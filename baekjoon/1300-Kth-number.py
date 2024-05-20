N = int(input())
k = int(input())

left = 0
right = N*N

while left <= right:
    mid = (left+right)//2
    sum = 0
    for i in range(N):
        sum += min(mid//(i+1), N)
    if sum < k:
        left = mid+1
    else:
        result = mid
        right = mid-1

print(result)
