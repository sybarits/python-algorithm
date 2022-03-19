def solution(A,B):
    answer = 0

    print('Hello Python')
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

if __name__ == "__main__":
    result = solution([1,4,2],[5,4,4])
    print(result)
