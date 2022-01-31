# 배열을 입력받아 output[i]가 자신을 제와한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
# 주의: 나눗셈을 하지 않고 O(n)에 풀이하라
class ProductOfArrayExceptSelf:

    def multiplyInOrder(self, nums: list[int]) -> list[int]:
        result = []

        for num in nums:
            temp = 1
            for num2 in nums:
                if num != num2:
                    temp *= num2
            result.append(temp)

        return result

    def leftAndRightMultiply(self, nums: list[int]) -> list[int]:
        pass
        # 풀이를 봐도 모르겠네...
        # 나중에 다시...



if __name__ == "__main__":
    pae = ProductOfArrayExceptSelf()
    print(pae.multiplyInOrder([1, 2, 3, 4]))
