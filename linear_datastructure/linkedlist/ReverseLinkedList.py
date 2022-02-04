# 연결 리스트를 뒤집어라
from ListNode import ListNode


class ReverseLinkedList:

    def reverseRecursive(self, node: ListNode, prev: ListNode = None) -> ListNode:
        if not node:
            return prev
        next, node.next = node.next, prev
        return self.reverseRecursive(next, node)

    def reverseLoop(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            node, prev = next, node

        return prev


if __name__ == "__main__":
    rl = ReverseLinkedList()
    l1 = ListNode(2, ListNode(3, ListNode(5, None)))
    rl.reverseRecursive(l1).printAll()
    l2 = ListNode(1, ListNode(2, ListNode(4, None)))
    rl.reverseLoop(l2).printAll()
