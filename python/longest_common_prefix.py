from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        if len(strs) >= 2:
            common = strs[0]
            while len(common) > 0:
                find = True
                for item in strs:
                    if item.find(common) != 0:
                        find = False
                        break
                if find is True:
                    break
                common = common[:-1]
        elif len(strs) == 1:
            common = strs[0]
        return common


ss = Solution()
print(ss.longestCommonPrefix("IV"))
