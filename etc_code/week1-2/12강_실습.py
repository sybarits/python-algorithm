# 중위표현 수식을 후위표현 수식으로 변환
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]
    
    def printAll(self):
        print(self.data)

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for char in S:
        if char == '(':
            opStack.push(char)
            continue
        if char == ')':
            while opStack.peek() != '(':
                answer += opStack.pop()
                if opStack.isEmpty():
                    break
            opStack.pop()
            continue
        if char not in prec:
            answer += char
            continue
        if opStack.isEmpty():
            opStack.push(char)
            continue
        while prec[opStack.peek()] >= prec[char]:
            answer += opStack.pop()
            if opStack.isEmpty():
                    break
        opStack.push(char)
    
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer

if __name__ == "__main__":
    print(solution("(A+B)*(C+D)"))#"AB+CD+*"
    print(solution("A*B+C"))#"AB*C+"
    print(solution("(A+B)*C"))#"AB+C*"