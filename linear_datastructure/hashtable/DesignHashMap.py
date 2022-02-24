# -*- coding: utf-8 -*-
# 다음의 기능을 제공하는 해시맵을 디자인하라.
# put(key, value): 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트한다.
# get(key): 키에 해당하는 가빗을 조회한다. 만약 키가 존재하지 않는다면 -1을 리턴
# remove(key): 키에 해당하는 키 값을 해기맵에서 삭제

# 개별 체이닝 방식(연결 리스트)을 이용한 해시 테이블 구현
import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        # defaultdict은 존재하지 않는 인덱스로 조회할 경우
        # 에러를 발생하지 않고 바로 디폴트 객체를 생성한다.

    def put(self, key: int, value: int):
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key,value)
            return
        
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int):
        index = key % self.size
        if self.table[index].value is None:
            return
        p = self.table[index]
        if p.key == key:
            if p.next is None:
                self.table[index] = ListNode()
            else:
                p.next
            return
        
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


if __name__ == "__main__":
    pass