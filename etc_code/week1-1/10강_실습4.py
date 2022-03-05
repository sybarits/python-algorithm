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


    def concat(self, L):
        self_last = self.tail.prev
        l_first = L.head.next
        self_last.next = l_first
        l_first.prev = self_last
        self.tail = L.tail
        self.nodeCount = self.nodeCount + L.nodeCount
        return self


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def traverse2(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result
    
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
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

    def print(self):
        curr = self.head
        while curr is not self.tail:
            print(curr.data, end="->")
            curr = curr.next
        print(self.tail.data)
    
    def print2(self):
        curr = self.tail
        while curr is not self.head:
            print(curr.data, end="->")
            curr = curr.prev
        print(self.head.data)

def solution(x):
    return 0

if __name__ == "__main__":
    L = DoublyLinkedList()
    L.insertAt(1,Node(1))
    L.insertAt(2,Node(2))
    L.insertAt(3,Node(3))

    L2 = DoublyLinkedList()
    L2.insertAt(1,Node(4))
    L2.insertAt(2,Node(5))

    L.concat(L2)
    L.print()
    L.print2()
    

