class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        previous = 0
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        for index in range(len(s) - 1, -1, -1):
            check = roman_map[s[index]]
            if check >= previous:
                result += check
                previous = check
            else:
                result -= check
        return result


ss = Solution()
print(ss.romanToInt("IV"))
