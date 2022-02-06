# 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라.
# 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.
from ListNode import ListNode


class OddEvenLinkedList:

    def solution(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd_root = head
        even_root = head.next
        even = even_root
        odd = odd_root

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_root
        return odd_root

    # 홀수 값 리스트 뒤에 짝수 값이 오도록 풀었네..
    def solution2(self, head: ListNode) -> ListNode:
        node = head
        even_root = ListNode()
        odd_root = ListNode()
        even = even_root
        odd = odd_root

        while node:
            if node.val % 2 == 1:
                odd.val = node.val
                odd.next = ListNode(None)
                odd = odd.next
            else:
                even.val = node.val
                even.next = ListNode(None)
                even = even.next

            node = node.next

        odd.val = even_root.val
        odd.next = even_root.next

        return odd_root


if __name__ == "__main__":
    oel = OddEvenLinkedList()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    oel.solution(l1).printAll()
    l2 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7, None)))))))
    oel.solution(l2).printAll()
