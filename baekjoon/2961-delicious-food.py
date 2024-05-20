n = int(input())

food = []
used = []
for i in range(n):
    s, b= map(int, input().split())
    food.append([s,b])
    used.append(False)

result = 99999999999
deff = 0

def cook(i, s, b):
    global n, food, deff, result

    for j in range(i,n):
        if not used[j]:
            deff = abs(s * food[j][0] - (b + food[j][1]))
            result = min(deff, result)
            used[j] = True
            cook(i+1, s * food[j][0] , b + food[j][1])
            used[j] = False

cook(0,1,0)
print(result)