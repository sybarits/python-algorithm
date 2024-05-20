import heapq


N, M = map(int, input().split())
arr = []
for i in range(N):
    temp = list(map(int, input().split()))
    temp.sort()
    for j in range(M):
        temp[j] = [temp[j], i]
    arr.append(temp)
    
index = [0] * N

hq = []
max_val = 0
for i in range(N):
    heapq.heappush(hq, arr[i][0])
    max_val = max(max_val, arr[i][0][0])

result = 10000000000

while True:
    # print(hq)
    p = heapq.heappop(hq)
    result = min(result, max_val - p[0])
    index[p[1]] += 1
    if index[p[1]] == M:
        break
    next = arr[p[1]][index[p[1]]]
    heapq.heappush(hq, next)
    max_val = max(max_val, next[0])

print(result)
