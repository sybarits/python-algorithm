# 연결 리스트를 입력받아 페어 단위로 스왑하라.
from ListNode import ListNode


class SwapNodesinPairs:

    def swapValues(self, head: ListNode) -> ListNode:
        node = head

        while node:
            n: ListNode = node.next
            node.val, n.val = n.val, node.val
            node = n.next

        return head

    def swapNodesLoop(self, head: ListNode) -> ListNode:
        node = head
        root = node.next
        p = ListNode(None)

        while node and node.next:
            n = node.next
            nn = node.next.next
            node.next, n.next = nn, node
            p.next = n
            # next step
            p = p.next.next
            node = nn

        return root

    def swapNodesRecursive(self, head: ListNode) -> ListNode:
        if head and head.next:
            node = head
            n = head.next
            head.next = self.swapNodesRecursive(n.next)
            n.next = head
            return n

        return head


if __name__ == "__main__":
    snp = SwapNodesinPairs()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
    snp.swapValues(l1).printAll()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
    snp.swapNodesLoop(l1).printAll()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
    snp.swapNodesRecursive(l1).printAll()