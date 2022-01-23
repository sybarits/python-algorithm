from typing import List  # python3.9 부터 내장 컬렉션 형을 제네릭으로 사용 가능함.list를 사용하면 임포트 안해도됨


class ReverseString:

    def twopointerswap(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)

    def pythonicway(self, s: str):
        s = s[::-1]
        print(s)


if __name__ == '__main__':
    rs = ReverseString()
    print(rs.twopointerswap(['h', 'e', 'l', 'l', 'o']))
    print(rs.pythonicway('hello'))
