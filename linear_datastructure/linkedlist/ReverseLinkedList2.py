# 인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m 은 1 부터 시작한다.
from ListNode import ListNode


class ReverseLinkedList2:

    def reverseLoop(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next


if __name__ == "__main__":
    rl = ReverseLinkedList2()
    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
    rl.reverseLoop(l2, 2, 4).printAll()
    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    rl.reverseLoop(l2, 2, 4).printAll()
