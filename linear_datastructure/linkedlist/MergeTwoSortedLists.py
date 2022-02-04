# 정렬되어 있는 두 연결 리스트를 합쳐라

from ListNode import ListNode


class MergeTwoSortedList:

    def linkResursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.linkResursive(l1.next, l2)
        return l1


if __name__ == "__main__":
    mt = MergeTwoSortedList()
    l1 = ListNode(1, ListNode(2, ListNode(4, None)))
    l2 = ListNode(2, ListNode(3, ListNode(5, None)))
    ll = mt.linkResursive(l1, l2)
    ll.printAll()
    print(ll, mt)
