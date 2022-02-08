# 괄호로 된 입력값이 올바른지 판별하라.

class ValidParantheses:

    def solution(self, sarr: str) -> bool:
        stack = []
        table = {')': '(', '}': '{', ']': '['}

        for s in sarr:
            if s not in table:
                stack.append(s)
            elif not stack or table[s] != stack.pop():
                return False

        return len(stack) == 0


if __name__ == "__main__":
    vp = ValidParantheses()
    print(vp.solution("(){}[]"))
    print(vp.solution("((){}[]"))
    print(vp.solution("()){}[]"))
    print(vp.solution("((()()){{}})[]"))
