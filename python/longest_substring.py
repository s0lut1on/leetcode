class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        old_longest = 0
        new_longest = ""
        for index in range(len(s)):
            new_longest = ""
            if s[index] not in new_longest:
                new_longest += s[index]
                new_index = index + 1
                while new_index < len(s) and s[new_index] not in new_longest:
                    new_longest += s[new_index]
                    new_index += 1
                if len(new_longest) > old_longest:
                    old_longest = len(new_longest)
            else:
                continue
        return old_longest


obj = Solution()
input_ = "pwwkew"
result = obj.lengthOfLongestSubstring(input_)
print("result: ", result)
