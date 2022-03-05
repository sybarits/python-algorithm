def solution(d, budget):
    d.sort()
    answer = 0
    for num in d:
        if budget - num >= 0:
            budget -= num
            answer += 1
        else:
            break

    return answer

if __name__ == "__main__":
    print(solution([1,3,2,5,4],9))
    print(solution([2,2,3,3],10))