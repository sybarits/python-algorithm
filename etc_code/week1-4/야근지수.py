class MaxHeap(object):
    def __init__(self):
        self.queue = [None]

    def insert(self, n):
        self.queue.append(n)
        for i in range(len(self.queue)//2, 0, -1):
            self.heapify(i)

    def remove(self):
        if len(self.queue) > 1:
            self.queue[1], self.queue[-1] = self.queue[-1], self.queue[1]
            data = self.queue.pop(-1)
            self.heapify(1)
        else:
            data = None
        return data
    
    def heapify(self, i):
        left = i * 2
        right = i * 2 + 1
        smallest = i
        if len(self.queue) > left and self.queue[left] > self.queue[smallest]:
            smallest = left
        if len(self.queue) > right and self.queue[right] > self.queue[smallest]:
            smallest = right
        if smallest != i:
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]
            self.heapify(smallest)

    def print_heap(self):
        print(self.queue)
    
    def minus(self):
        self.queue[1] -= 1
        self.heapify(1)
    
    def getQueue(self):
        return self.queue[1:]

    def empty(self):
        return len(self.queue) == 1

def solution(n, works):
    answer = 0
    mh = MaxHeap()

    if sum(works) <= n:
        return 0

    for num in works:
        mh.insert(num)
    
    while n > 0:
        mh.minus()
        n -= 1
    
    mh.print_heap()
    q = mh.queue[1:]
    for n in q:
        answer += n*n

    # while not mh.empty():
    #     answer += mh.remove()**2
    
    return answer

if __name__ == "__main__":

    
    print("wow")
    # print(solution(4,[4,3,3]))#12
    # print(solution(8,[1,5,5]))#3
    print(solution(8,[5,1,5,5]))#18
    print(solution(8,[2,1,2,2]))#0
    # print(solution(8,[2,1,2,2]))#0
    # print(solution(1,[2,1,2]))#6
    # print(solution(3,[1,1]))#0
    print(solution(4,[50000 for _ in range(20)]))