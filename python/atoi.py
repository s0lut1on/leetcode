import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = re.sub(r"[^\d\.\-]+", "", s)
        result = int(s)
        if result > pow(2, 31) - 1 or result < pow(-2, 31):
            return 0
        else:
            return result


ss = Solution()
print(ss.myAtoi("1234asc"))