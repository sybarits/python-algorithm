# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
# 애너그램은 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 의미한다.
import collections


class GroupAnagrams:

    def sortDictionary(self, words: list[str]) -> list[list[str]]:
        words_dict = collections.defaultdict(list)
        # defaultdict()은 키에 해당하는 값을 기본으로 지정해준다.
        # 인자가 아무것도 없으면 키에 해당하는 값은 0이고
        # list로 한다면 기본값은 [] 이다.
        # dict은 존재하지 않는 키에 값을 삽입하려 하면 keyerror가 발생하지만
        # defaultdict() 은 항상 기본값을 생성해주어 해당 키값이 존재하는지 확인하는 조건문 생략이 가능하다.

        for word in words:
            words_dict[''.join(sorted(word))].append(word)

        # sorted(__iterable)은 정령한 결과를 리스트로 반환한다.
        # ''.join(__iterable)은 문자열로 변환할 수 있다.
        # list.sort() 는 list를 정렬(In-place Sort)한다. 별도의 저장 공간이 필요없다.

        return words_dict.values()


if __name__ == '__main__':
    sd = GroupAnagrams()
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sd.sortDictionary(words))
