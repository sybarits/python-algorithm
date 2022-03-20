class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size() + self.stack2.size()

    def push(self, item):
        if self.qsize() == self.max_size:
            return False
        self.stack1.push(item)
        return True

    def pop(self):
        if self.qsize() == 0:
            # raise EmptyException
            return False

        if self.stack2.size() == 0:
            while self.stack1.size() != 0:
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()

class EmptyException(Exception):
    def __init__(self):
        super().__init__('Queue is empty')

# q = MyQueue(1)
# q.push(int("3"))
# print("pop",q.pop())


n, max_size = map(int, input().strip().split(' '))
q = MyQueue(max_size)
# print(n, max_size)
for i in range(n):
    std_in = input().strip().split(' ')
    if std_in[0] == "PUSH":
        print(q.push(int(std_in[1])))
    elif std_in[0] == "POP":
        try:
            print(q.pop())
        except EmptyException as e:
            print(e)
    elif std_in[0] == "SIZE":
        print(q.qsize())
    else:
        pass
