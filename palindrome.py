class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = abs(x)
        revert_x = int(str(x)[::-1])
        if revert_x - x == 0:
            return True
        return False

ss = Solution()
print(ss.isPalindrome(-121))