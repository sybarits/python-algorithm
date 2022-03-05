# 최대 힙에서의 원소 삭제
class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)

        item_index = self.data.index(item)

        while item_index > 0:
            parent_index = item_index//2
            if parent_index > 0 and self.data[parent_index] < self.data[item_index]:
                self.data[parent_index], self.data[item_index] = self.data[item_index], self.data[parent_index]
            item_index = parent_index

    def items(self):
        print(self.data)

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def sort(self):
        arr = []
        d = self.remove()

        while d:
            arr.append(d)
            d = mh.remove()
        
        return arr


    def maxHeapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = i*2
        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = i*2+1
        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if len(self.data) > left and self.data[left] > self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            smallest = left
        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if len(self.data) > right and self.data[right] > self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest = right
        if smallest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)


def solution(x):
    return 0

if __name__ == "__main__":
    mh = MaxHeap()
    mh.insert(2)
    mh.items()
    mh.insert(3)
    mh.items()
    mh.insert(9)
    mh.items()
    mh.insert(8)
    mh.items()
    mh.insert(5)
    mh.items()
    
    print(mh.sort())

    mh.items()