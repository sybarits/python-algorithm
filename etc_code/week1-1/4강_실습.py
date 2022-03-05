def solution(x):
    answer = 0
    if x == 0:
        return 0
    if x == 1:
        return 1
    return solution(x - 1) + solution(x - 2)

def solution2(x):
    f1, f2 = 0, 1
    f3 = 0
    arr = [f1,f2]
    if x == 0:
        return f1
    if x == 1:
        return f2

    for i in range(2,x+1):
        arr.append(arr[i-1] + arr[i-2])
    
    return arr[-1]

def solution3(x):
    f1, f2 = 0, 1
    f3 = 0
    if x == 0:
        return f1
    if x == 1:
        return f2

    for _ in range(2,x+1):
        f3 = f1 + f2
        f1, f2 = f2, f3
    
    return f3

if __name__ == "__main__":
    print(solution(6))
    print(solution2(6))
    print(solution3(6))