# 로그 재 정렬
# 1. 로그의 가장 앞 부분은 식별자다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.
class ReorderLogFiles:

    def lambda_plus(self, strl: list[str]) -> list[str]:
        logs = strl
        result, digit = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                result.append(log)

        result.sort(key=lambda x: (x.split()[1], x.split()[0]))
        # 리스트 정렬 함수로 sort 사용
        # .sort() 로 사용하면 오름차순 정렬
        # .sort(reverse=True) 로 사용하면 내림차순 정렬
        # .sort(key=lambda x: (~~)) 로 사용하면 ~~ 내에 있는 값을 기준으로 오름차순 정렬
        # def foo(x):
        #     return x.split()[1], x.split()[0]
        # .sort(key=foo) 를 위처럼 람다로 한줄로 줄여 쓸 수 있다.
        # foo 함수는 정렬에 사용될 키 두개를 반환한다.

        return result + digit


if __name__ == '__main__':
    rlf = ReorderLogFiles()
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(rlf.lambda_plus(logs))
