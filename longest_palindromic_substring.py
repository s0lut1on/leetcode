class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        for first in range(len(s) - 1):
            for last in range(len(s) - 1, first, -1):
                if s[first] == s[last]:
                    new_first = first + 1
                    new_last = last - 1
                    while new_first <= new_last and s[new_first] == s[new_last]:
                        new_first += 1
                        new_last -= 1
                    if new_first > new_last:
                        return s[first:last+1]
                    else:
                        continue
                else:
                    continue
        return s[0]


obj = Solution()
input_ = "cbbd"
result = obj.longestPalindrome(input_)
print("result: ", result)
