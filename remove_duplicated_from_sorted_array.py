from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        previous = nums[len(nums) - 1]
        for index in range(len(nums) - 2, -1, -1):
            if nums[index] == previous:
                del nums[index]
                nums.append("_")
                index += 1
            else:
                previous = nums[index]
                counter += 1
        return counter

ss = Solution()
input_list = [1, 1, 2, 2]
print(ss.removeDuplicates(input_list))
print(input_list)