class TrappingRainWater:

    def twoPointer(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        volume = 0

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

    def stackPop(self, height: list[int]) -> int:
        pass
        # 스택을 이용한 문제는 내공을 더 쌓고 도전하겠다.
            


if __name__ == "__main__":
    trw = TrappingRainWater()
    print("volume is", trw.twoPointer([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
