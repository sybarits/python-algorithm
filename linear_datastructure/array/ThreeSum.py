class ThreeSum:

    def bruteForce(self, nums: list[str]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] == 0 and nums[j] == 0 and nums[k] == 0:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])

        return result

    # 부르트 포스로 계산하면 O(n^3)
    # 투 포인터로 계산하면 O(n^2)

    def twoPointer(self, nums: list[str]) -> list[list[int]]:
        result = []
        left, right = 0, 0
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] == 0 and nums[left] == 0 and nums[right] == 0:
                    break
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 중복값 처리 while 문
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result


if __name__ == '__main__':
    ts = ThreeSum()
    print(ts.bruteForce([-1, 0, 1, 2, -1, -4, 0, 0, 1, 1]))
    print(ts.twoPointer([-1, 0, 1, 2, -1, -4, 0, 0, 1, 1]))
