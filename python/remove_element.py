from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int], val: int) -> int:
        counter = 0
        for index in range(len(nums) - 1, -1, -1):
            if nums[index] == val:
                del nums[index]
                nums.append("_")
                index += 1
            else:
                counter += 1
        return counter


ss = Solution()
input_list = [1, 1, 2, 2]
print(ss.removeDuplicates(input_list, 2))
print(input_list)