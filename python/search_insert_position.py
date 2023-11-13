from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        position = nums.index(target)
        if position > -1:
            return position
        else:
            