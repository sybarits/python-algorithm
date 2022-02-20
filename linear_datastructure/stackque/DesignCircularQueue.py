# 원형 큐를 디자인하라.
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, val: int) -> bool:
        if self.q[self.p2] == None:
            self.q[self.p2] = val
            self.p2 = (self.p2 +1 )%self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1] == None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        if self.q[self.p1] == None:
            return -1
        else:
            return self.q[self.p1]

    def Rear(self) -> int:
        if self.q[self.p2-1] == None:
            return -1
        else:
            return self.q[self.p2 -1]

    def empty(self) -> bool:
        if self.p1 == self.p2 and not self.q[self.p1]:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.p1 == self.p2 and self.q[self.p1]:
            return True
        else:
            return False



if __name__ == "__main__":
    circularQueue = MyCircularQueue(5)
    print(circularQueue.enQueue(2))
    print(circularQueue.enQueue(1))
    print(circularQueue.enQueue(5))
    print(circularQueue.enQueue(6))
    print(circularQueue.Rear())
    print(circularQueue.enQueue(9))
    print(circularQueue.empty())
    print(circularQueue.isFull())
    print(circularQueue.Front())
    print(circularQueue.deQueue())
    print(circularQueue.Front())
