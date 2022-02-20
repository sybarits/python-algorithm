# 다음 연산을 제공하는 원형 데크를 디자인하라.
# MyCirculaDeque(k): 데크사이즈를 지정하는 생성자
# insertFront(): 데크 처음에 아이템을 추가하고 성공할 경우 참을 리턴
# insertLast(): 데크 마지막에 아이템을 추가하고 성공할 경우 참을 리턴
# deleteFront(): 데크 처음에 아이템을 삭제하고 성공할 경우 참을 리턴
# deleteLast(): 데크 마지막에 아이템을 삭제하고 성공할 경우 참을 리턴
# getFront(): 데크의 첫 번째 아이템을 가져온다. 데크가 비어 있다면 -1 리턴
# getRear(): 데크의 마지막 아이템을 가져온다. 데크가 비어 있다면 -1 리턴
# isEmpty(): 데크가 비어 있는지 여부를 판별한다.
# isFull(): 데크가 가득 차 있는지 여부를 판별한다.

# deque는 double ended queue 의 약자로 양쪽 끝 모두에서 queue 연산이 가능

class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class MyCirculaDeque:
    def __init__(self, k: int):
        self.haed, self,tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        r = node.right
        node.right = new
        new.left = node
        r.left = node
        node.right = r

    def _del(self, node:ListNode):
        l = node.left.left
        node.right = l
        l.left = node

    def insertFront(self, val: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.haed, ListNode(val))
        return True

    def insertLast(self, val: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(val))
        return True

    def deleteFront(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.haed)
        return True

    def deleteLast(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        if self.len == 0:
            return -1
        return self.haed.right.val

    def getRear(self) -> int:
        if self.len == 0:
            return -1
        return self.tail.left.val

    def isEmpty(self):
        return self.len == 0

    def isFull(self):
        return self.len == self.k
