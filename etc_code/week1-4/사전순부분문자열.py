def solution(s):
    stack = []
    for c in s:
        print(stack)
        while stack and stack[-1] < c:
            stack.pop()
        stack.append(c)
    return ''.join(stack)

if __name__ == "__main__":
    print(solution("xyb"))
    print(solution("yxyc"))