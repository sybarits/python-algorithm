# 연결 리스트가 팰린드롬 구조인지 판별하라
import collections
from typing import Deque

from ListNode import ListNode


class PalindromeLinkedList:

    def listChange(self, head: ListNode) -> bool:
        q: list = []

        if not head:
            return True

        node = head
        # 배열로 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # return q == q[::-1]
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

    def useDeque(self, head: ListNode) -> bool:
        q: Deque = collections.deque()
        # deque는 pop(0)을 상수 복잡도로 연산한다.
        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():  # pop(0) 대신 popleft() 사용
                return False

        return True

    def useRunner(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # 두칸씩 뛰는 fast runner를 사용해 slow runner를 데이터의 중간에 위치한 곳까지 가도록 한다.
        # rev는 slow를 데이터 중간까지 이동하면서 순서를 뒤집어 연결 리스트를 만든다.
        if fast:
            slow = slow.next

        # slow runner는 중간 이후로 위치시킨 상태에서 rev와 비교한다.
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


if __name__ == "__main__":
    pl = PalindromeLinkedList()
    head = ListNode(1, ListNode(2, None))
    print(pl.listChange(head))
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
    print(pl.listChange(head))
    head = ListNode(1, ListNode(2, None))
    print(pl.useDeque(head))
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
    print(pl.useDeque(head))
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
    print(pl.useRunner(head))
