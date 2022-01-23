# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
import collections
import re


class ValidPalindrome:

    def __init__(self):
        pass

    def using_list(self, s: str) -> bool:
        s_list = []
        for char in s:
            if char.isalnum():
                s_list.append(char.lower())

        while len(s_list) > 1:
            if s_list.pop(0) != s_list.pop():
                return False

        return True

    def using_deque(self, s: str) -> bool:
        s_list = collections.deque()
        for char in s:
            if char.isalnum():
                s_list.append(char.lower())

        while len(s_list) > 1:
            if s_list.popleft() != s_list.pop():
                return False

        return True

    def using_slicing(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


if __name__ == '__main__':
    p = ValidPalindrome()
    print(p.using_list("A man, a plan, a canal: Panama"))
    print(p.using_deque("A man, a plan, a canal: Panama"))
    print(p.using_slicing("A man, a plan, a canal: Panama"))
