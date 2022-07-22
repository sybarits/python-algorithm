
n = int(input())

garden = [[0]*n for _ in range(n)]
flower = [[0]*n for _ in range(n)]

for i in range(n):
    garden[i] = list(map(int, input().split()))

# print("garden")
# print(garden)
total = 0
result = 99999999

def plant(seed):
    global total, result

    if seed == 3:
        result = min(total, result)
        return
    
    for i in range(1,n-1):
        for j in range(1,n-1):
            if flower[i][j] != 1 and flower[i-1][j] != 1 \
                and flower[i+1][j] != 1 and flower[i][j-1] != 1 \
                and flower[i][j+1] != 1:
                sum = garden[i][j] + garden[i-1][j] + garden[i+1][j] + garden[i][j-1] + garden[i][j+1]
                total += sum
                flower[i][j] = 1
                flower[i-1][j] = 1
                flower[i+1][j] = 1
                flower[i][j-1] = 1
                flower[i][j+1] = 1

                plant(seed+1)

                total -= sum
                flower[i][j] = 0
                flower[i-1][j] = 0
                flower[i+1][j] = 0
                flower[i][j-1] = 0
                flower[i][j+1] = 0

plant(0)

print(result)
                