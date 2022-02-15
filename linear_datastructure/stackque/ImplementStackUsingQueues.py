# 큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
# push(x): 요소 x를 스택에 삽입한다.
# pop(): 스택의 첫 번째 요소를 삭제한다.
# top(): 스택의 첫 변째 요소를 가져온다.
# empty(): 스택이 비어 있는지 여부를 리턴한다.
import collections


class ImplementStackUsingQueues:
    def __init__(self):
        self.q = collections.deque()

    # 큐 자료구조와 큐에서 사용하는 메소드만을 이용해
    # 스택 자료구조와 스택에서 사용하는 메소드를 구현한다.
    # push를 할 때 큐 맨 뒤에 자료를 입력하고
    # 앞에 있던 자료들을 차례로 빼서 맨뒤로 차곡차곡 입력한다.
    # 그러면 큐에 가장 나중에 들어간 자료가 큐에 가장 앞에 자리한다.
    def push(self, item):
        # self.q.appendleft(item)
        self.q.append(item)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

    def items(self):
        print(self.q)


if __name__ == "__main__":
    isq = ImplementStackUsingQueues()
    isq.push(1)
    isq.push(2)
    isq.push(3)
    isq.push(4)
    isq.items()
    print(isq.top())
    print(isq.pop())
    isq.items()
