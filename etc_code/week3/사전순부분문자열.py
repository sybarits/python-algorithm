def solution(s):
    stack = []
    for c in s:
        while stack and stack[-1] < c:
            stack.pop()
        stack.append(c)
    return ''.join(stack)


if __name__ == "__main__":
    for i in range(1,101):
        input_file = ""
        answer_file = ""
        if i < 10:
            input_file = "0"+str(i)
        else:
            input_file = str(i)
        answer_file = input_file+".a"
        input_f = open(input_file, 'r')
        answer_f = open(answer_file, 'r')
        result = solution(input_f.readline().strip())
        answer = answer_f.readline().strip()
        # print("input_file",input_file,"answer_file",answer_file, result, answer)
        print(input_file, result == answer)


        