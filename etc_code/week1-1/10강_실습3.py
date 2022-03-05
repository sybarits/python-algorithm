class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount+1:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        if prev == self.tail:
            return None
        next = prev.next.next
        node = prev.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return node.data


    def popBefore(self, next):
        if next == self.head:
            return None
        prev = next.prev.prev
        node = next.prev
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return node.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos-1)
        return self.popAfter(prev)
    
    def popAt2(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos+1)
        return self.popBefore(prev)


    def print(self):
        curr = self.head
        while curr is not self.tail:
            print(curr.data, end="->")
            curr = curr.next
        print(self.tail.data)

def solution(x):
    return 0

if __name__ == "__main__":
    L = DoublyLinkedList()
    a = Node(67)
    b = Node(34)
    c = Node(27)
    L.insertAt(1,a)
    L.insertAt(2,b)
    L.insertAt(3,c)
    # node = L.popAfter(b)
    # print(node)
    # L.print()
    node = L.popAt(3)
    print(node)
    L.print()
    # print(L.reverse())