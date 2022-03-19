def solution(s):
    answer = 0
    slen = len(s)
    if len(s) == 1 or s == s[::-1]:
        return len(s)

    for l in range(slen, 0 , -1):
        for i in range(0,slen-l+1):
            temp = s[i:l+i]
            print(l, i, temp)
            if temp == temp[::-1]:
                answer = l
                break
        if answer == l:
            break

    print(answer)
    return answer


if __name__ == "__main__":
    solution("abcdcba")
    solution("abacde")