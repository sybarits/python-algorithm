# 스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
# push(x): 요소 x를 큐 마지막에 삽입한다.
# pop(): 큐 처음에 있는 요소를 삭제한다.
# peek(): 큐 처음에 있는 요소를 가져온다.
# empty(): 큐가 비어 있는지 여부를 리턴한다.

class ImplementQueueUsingStacks:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, item):
        self.input.append(item)

    def pop(self):
        self.peek()
        return self.output.pop()

    # 스택에 들어간 자료를 꺼내어 다른 스택(output)에 넣으면
    #  output 스택의 맨위에는 가장 먼저 들어간 자료가 위치한다.
    # 따라서 자료구조에 들어간 자료를 빼는 것을 시도할 때는 언제나
    # input 스택에 있는 자료들을 output 스택으로 옮겨 꺼낼 수 있도록 준비해둔다.
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []

    def items(self):
        self.peek()
        while self.output:
            self.input.append(self.output.pop())
        print(self.input)


if __name__ == "__main__":
    isq = ImplementQueueUsingStacks()
    isq.push(1)
    isq.push(2)
    isq.push(3)
    isq.push(4)
    isq.items()
    print(isq.peek())
    print(isq.pop())
    isq.items()