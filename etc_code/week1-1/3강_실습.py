def solution(L, x):
    answer, middle = 0, 0
    left, right = 0, len(L) - 1
    
    # if x not in L:
    #     return -1

    while left <= right:
        middle = (left + right) // 2
        # print("m",middle, "l", left, "r", right)
        if L[middle] == x:
            return middle
        elif L[middle] < x:
            left = middle + 1
        elif L[middle] > x:
            right = middle - 1
        
    return -1

if __name__ == "__main__":
    print(solution([2, 3, 5, 6, 9, 11, 15], 15))
    print(solution([2, 5, 7, 9, 11], 4))
    print(solution([1,2,3], 3))