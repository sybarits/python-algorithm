def solution(L, x):
    answer = []
    
    if x not in L:
        return [-1]
    
    for i, num in enumerate(L):
        if x == num:
            answer.append(i)
    
    if len(answer) == 0:
        answer.append(-1)
        
    return answer

if __name__ == "__main__":
    print(solution([64, 72, 83, 72, 54], 72))