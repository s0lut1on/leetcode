from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for start in range(0, len(height) - 1):
            for end in range(len(height) - 1, start, -1):
                area = min(height[start], height[end]) * (end - start)
                if area > max_area:
                    max_area = area
        return max_area


ss = Solution()
print(ss.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
