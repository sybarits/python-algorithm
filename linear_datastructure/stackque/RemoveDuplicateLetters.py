# 중복된 문자를 제외하고 사전식 순서(lexicographical order)로 나열하라.
import collections


class RemoveDuplicateLetters:

    def recursivelySolution(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.recursivelySolution(suffix.replace(char,''))
        return ''

    def stackSolution(self, s: str) -> str:
        counter, stack = collections.Counter(s), []
        print(counter)
        # 이거 모르겠네...
        return ''.join(stack)




if __name__ == "__main__":
    rdl = RemoveDuplicateLetters()

    print(rdl.recursivelySolution("bcabc"))
    print(rdl.recursivelySolution("cbacdcbc"))
    print(rdl.stackSolution("cbacdcbc"))

