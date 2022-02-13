# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
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

    # 와... 너무 어렵다... 이거 다시 풀어보라고 하면 풀 수 있을까...
    def stackPop(self, height: list[int]) -> int:
        stack = []
        total_volume = 0

        for i, curH in enumerate(height):
            while stack and curH > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                waters = min(height[stack[-1]], curH) - height[top]
                # 이미 처리한 물을 제외하기 위해 height[top]를 빼준다.
                # min을 하는 이유는 둘중에 낮은 것을 기준으로 물 수위가 결정 되기 때문에
                water_volume = waters * (i - stack[-1] - 1)
                # i - stack[-1] - 1 은 얼마나 떨어진 블럭을 기준으로 할 건지에 대한 값이다.
                total_volume += water_volume
            stack.append(i)

        return total_volume


if __name__ == "__main__":
    trw = TrappingRainWater()
    print("volume is", trw.twoPointer([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trw.stackPop([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
