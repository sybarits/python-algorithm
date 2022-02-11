# 매일 화씨 온도 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

class DailyTemperatures:

    def mySolution(self, T: list) -> list:

        result = [0 for _ in range(len(T))]
        for i, t in enumerate(T):
            for j, t2 in enumerate(T):
                if j > i and t < t2:
                    result[i] = (j - i)
                    break
        # 이렇게 풀면 불필요한 순회(i > j 구간)를 하기 때문에 비효율 적이다.
        return result

    # 스택을 이용한 풀이는 불필요한 구간 순회를 하지 않고 해결 할 수 있다.
    # 더 아름답다... 외워라...
    def stackSolution(self, T: list) -> list:
        result, stack = [0 for _ in range(len(T))], []

        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)

        return result


if __name__ == "__main__":
    dt = DailyTemperatures()
    print(dt.mySolution([73, 74, 75, 71, 69, 72, 76, 73]))
    print(dt.stackSolution([73, 74, 75, 71, 69, 72, 76, 73]))
