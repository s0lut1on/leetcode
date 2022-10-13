from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_index = list(range(len(nums)))
        nums, list_index = list(zip(*sorted(zip(nums, list_index))))
        nums = list(nums)
        list_index = list(list_index)
        print(nums)
        print(list_index)
        for end in range(len(nums) - 1, 0, -1):
            for start in range(0, end):
                sum_ = nums[start] + nums[end]
                if sum_ == target:
                    return [list_index[start], list_index[end]]
                elif sum_ < target:
                    continue
        return []


ss = Solution()
print(ss.twoSum([-3, 4, 3, 90], 0))
