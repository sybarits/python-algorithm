# 후위표현 수식 계산
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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if token == '(':
            opStack.push(token)
            continue
        if token == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
                if opStack.isEmpty():
                    break
            opStack.pop()
            continue
        if type(token) is int:
            postfixList.append(token)
            continue
        if opStack.isEmpty():
            opStack.push(token)
            continue
        while prec[opStack.peek()] >= prec[token]:
            postfixList.append(opStack.pop())
            if opStack.isEmpty():
                    break
        opStack.push(token)
    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack = ArrayStack()

    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        else:
            a = valStack.pop()
            b = valStack.pop()
            #  a와 b의 순서 중요
            if token == '*':
                valStack.push(b*a)
            elif token == '/':
                valStack.push(b/a)
            elif token == '+':
                valStack.push(b+a)
            elif token == '-':
                valStack.push(b-a)
        
    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

if __name__ == "__main__":
    print(solution("5 + 3")) # 8
    print(solution("(1 + 2) * (3 + 4)")) # 21
    print(solution("7 * (9 - (3+2))")) # 28
