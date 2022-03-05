#!/usr/bin/python3
import heapq

def solution(n, works):
    answer = 0
    mh = []

    if sum(works) <= n:
        return 0

    for i in works:
        heapq.heappush(mh,i * (-1))
    
    temp = 1
    while n != 0:
        temp = heapq.heappop(mh)
        temp *= -1
        temp -= 1
        heapq.heappush(mh,temp*(-1))
        n -= 1

    for n in mh:
        answer += n*n
    
    return answer


if __name__ == "__main__":
    print(solution(4, [4,3,3]))
    print(solution(4, [1,2,3]))
    print(solution(4, [1,1]))