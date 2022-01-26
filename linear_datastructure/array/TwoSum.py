# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
class TwoSum:

    def bruteForce(self, nums: list[int], target: int) -> list[int]:
        result = []

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

        return result

    def inSearch(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            num = target - n
            if num in nums[i+1:]:
                return [i, nums.index(num)]

    def keySearch(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}

        for i, n in enumerate(nums):
            nums_map[n] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums.index(target - num)]
        # dictionary를 이용하면 if in 연산이 (거의) O(1) 이다.
        # inSearch에서 사용하는 if in 연산은 O(n) 이다.
        # dictionary는 해시 테이블로 구현 되어있기 때문이다.


    # def keySearch(self, nums: list[int], target: int) -> list[int]:
    # def keySearch(self, nums: list[int], target: int) -> list[int]:
    # def keySearch(self, nums: list[int], target: int) -> list[int]:

if __name__ == "__main__":
    ts = TwoSum()
    print(ts.bruteForce([2, 7, 11, 15], 9))
    print(ts.inSearch([2, 7, 11, 15], 9))
    print(ts.keySearch([2, 7, 11, 15], 9))

