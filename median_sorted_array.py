from typing import List
import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        if len(nums1) == 0:
            return 0
        elif len(nums1) % 2 != 0:
            return nums1[math.floor(len(nums1) / 2)]
        else:
            median_index = int(len(nums1) / 2)
            return (nums1[median_index] + nums1[median_index - 1]) / 2


obj = Solution()
result = obj.findMedianSortedArrays([1, 3], [2, 4])
print("result: ", result)
