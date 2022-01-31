# n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
class ArrayPartition1:

    def ascendingOrder(self, nums: list[int]) -> int:
        result = 0
        nums.sort(reverse=True)

        for i in range(0, len(nums), 2):
            result += min(nums[i], nums[i + 1])

        return result

    def evenNumbers(self, nums: list[int]) -> int:
        result = 0
        nums.sort()

        for i, num in enumerate(nums):
            if i % 2 == 0:
                result += num

        return result

    # slice를 이용할 때 :2를 추가하면 짝수번째 요소만 반환한다.
    def pythonicWay(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])

# 이 문제는 문제를 이해하는 것이 어렵구나
# 이해하면 빠른 풀이가 가능
if __name__ == "__main__":
    ap = ArrayPartition1()
    print("result is", ap.ascendingOrder([1, 4, 3, 2]))
    print("result is", ap.evenNumbers([1, 4, 3, 2]))
    print("result is", ap.pythonicWay([1, 4, 3, 2]))
