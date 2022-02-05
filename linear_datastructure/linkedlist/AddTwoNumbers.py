# 역순으로 저장된 연결리스트의 숫자를 더하라.
from ListNode import ListNode


class AddTwoNeumbers:

    def changeType(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = result = ListNode()
        hi = 0
        ra = []

        while l1 and l2:
            num = l1.val + l2.val
            ra.append(num%10 + hi)
            l1, l2 = l1.next, l2.next
            if num / 10 >= 1:
                hi = 1
            else:
                hi = 0
        ra.reverse()
        prev: ListNode = None
        for num in ra:
            node = ListNode(num)
            node.next = prev
            prev = node

        return node

    def fullAdder(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = result = ListNode()
        carry = 0
        while l1 and l2:
            num = l1.val + l2.val
            l1, l2 = l1.next, l2.next
            carry, val = divmod(num + carry, 10)
            node.val = val
            if l1 and l2:
                node.next = ListNode()
                node = node.next

        return result


if __name__ == "__main__":
    atn = AddTwoNeumbers()
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    atn.changeType(l1, l2).printAll()
    atn.fullAdder(l1, l2).printAll()
