class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        longest_result = s[0]
        for first in range(len(s) - 1):
            for last in range(len(s) - 1, first, -1):
                if s[first] == s[last]:
                    left_start = first
                    right_end = last+1
                    left_end = first + (last+1-first) // 2
                    right_start = first + (last+1-first) // 2 + 1

                    if (last+1-first) % 2 == 0:
                        left_end = first + int((last+1-first) / 2)
                        right_start = first + int((last+1-first) / 2)

                    left = s[left_start:left_end]
                    right = s[right_start:right_end]
                    if left == right[::-1] and last+1-first > len(longest_result):
                        longest_result = s[first:last+1]
                    else:
                        continue
                else:
                    continue
        return longest_result


obj = Solution()
input_ = "bdcedb"
result = obj.longestPalindrome(input_)
print("result: ", result)
