# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.
import collections
import re


class MostCommonWord:

    def listCounter(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        # list comprehention 리스트 컴프리헨션은 리스트 생성시 사용하는 파이썬 문법이다.
        # 예시 ll = [(x,y,z) for x in range(5) for y in range(5) if x != y for z in range(5) if y != z]
        count = collections.Counter(words)
        return count.most_common(1)[0][0]


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    mcw = MostCommonWord()
    print(mcw.listCounter(paragraph, banned))
