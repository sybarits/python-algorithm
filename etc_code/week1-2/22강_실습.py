# 최대 힙에 새로운 원소 삽입
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


def solution(x):
    return 0

if __name__ == "__main__":
    mh = MaxHeap()
    mh.insert(5)
    mh.items()
    mh.insert(6)
    mh.items()
    mh.insert(7)
    mh.items()
    mh.insert(8)
    mh.items()
    mh.insert(1)
    mh.items()

