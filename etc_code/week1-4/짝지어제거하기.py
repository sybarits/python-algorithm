def solution(s):
    answer = 0
    cstack = []
    
    for char in s:
        if len(cstack) == 0:
            cstack.append(char)
            continue
        if cstack[-1] == char:
            cstack.pop()
            continue
        cstack.append(char)
    
    if len(cstack) == 0:
        answer = 1

    return answer


if __name__ == "__main__":
    # s = "abcdefg"
    # print(s[3:2])
    # print(s[1])
    # print(s[0:0] + s[2:])
    s = "aa"
    print(solution(s))
    print(solution("baabaa"))
    print(solution("cdcd"))
