# k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라
# 1->4->5
# 1->3->4
# 2->6

# 결과 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printVal(self, node):
        if node and node.next:
            print(node.val, "->", end=' ')
            node.next.printVal(node.next)
        if node and not node.next:
            print(node.val)

    def printAll(self):
        self.printVal(self)


class MergekSortedList:
    def __init__(self):
        pass

    def do(self, lists: list[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []
        print(lists)

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            i = node[1]
            result.next = node[2]
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, i, result.next))

        return root.next

if __name__ == "__main__":
    msl = MergekSortedList()
    lists = [ListNode(1, ListNode(4, ListNode(5))),
             ListNode(1, ListNode(3, ListNode(4))),
             ListNode(2, ListNode(6))]
    node = msl.do(lists)
    node.printAll()
