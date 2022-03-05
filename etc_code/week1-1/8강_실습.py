class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        if pos == 1 and self.nodeCount == 1:
            node = self.head
            self.head = None
            self.tail = None
            self.nodeCount = 0
            return node
        
        if pos == 1:
            node = self.head
            self.head = self.head.next
            self.nodeCount -= 1
            return node
        
        if pos == self.nodeCount:
            node = self.tail
            self.tail = self.getAt(pos-1)
            self.nodeCount -= 1
            return node

        prev = self.getAt(pos - 1)
        node = prev.next
        prev.next = node.next
        self.nodeCount -= 1
        return node



    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    def print(self):
        curr = self.head
        while curr is not self.tail:
            print(curr.data, end="->")
            curr = curr.next
        print(self.tail.data)


def solution(x):
    return 0

if __name__ == "__main__":
    L = LinkedList()
    L.insertAt(1,Node(67))
    L.insertAt(2,Node(34))
    L.insertAt(3,Node(27))
    node = L.popAt(3)
    print(node)
    L.print()