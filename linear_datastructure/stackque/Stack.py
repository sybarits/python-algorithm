# 연결 리스트를 이용한 스택 ADT(abstract data type) 구현
from linear_datastructure.stackque.Node import Node


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        if not self.last:
            return None
        item = self.last.item
        self.last = self.last.next
        return item

    def printVal(self, node):
        if node and node.last:
            print(node.pop(), "->", end=' ')
            node.printVal(node)
            return
        if node and not node.last:
            print(node.pop())
            return

    def printAll(self):
        self.printVal(self)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.printAll()
