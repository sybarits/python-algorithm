N, K = map(int, input().split())

# print(N, K)


arr = list(map(int, input().split()))
num_check = [0 for _ in range(max(arr)+1)]

max_len = 0
start, end, = 0, 0

while end < N:
    if num_check[arr[end]] < K:
        num_check[arr[end]] += 1
        end += 1
    else:
        num_check[arr[start]] -= 1
        start += 1
    max_len = max(max_len, end - start)

print(max_len)

