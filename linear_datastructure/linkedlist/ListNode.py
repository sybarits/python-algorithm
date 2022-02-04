class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def list_init(self, ll: list[int]):
        ln = None
        for n in ll[::-1]:
            ln = ListNode(n, ln)

    def printVal(self, node):
        if node and node.val and node.next:
            print(node.val, "->", end=' ')
            node.next.printVal(node.next)
        if node and not node.next:
            print(node.val)


    def printAll(self):
        self.printVal(self)