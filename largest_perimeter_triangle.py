from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if len(nums) < 3 or len(nums) > pow(10, 4):
            return 0
        for item in nums:
            if item < 1 or item > pow(10, 6):
                return 0
        for index1 in range(0, len(nums) - 2):
            if self.is_triangle(nums[index1], nums[index1 + 1], nums[index1 + 2]):
                return nums[index1] + nums[index1 + 1] + nums[index1 + 2]
        return 0

    def is_triangle(self, a, b, c):
        if a >= b + c:
            return False
        return True


if __name__ == "__main__":
    ss = Solution()
    print(ss.largestPerimeter([2, 1, 2]))
