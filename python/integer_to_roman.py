class Solution:
    def intToRoman(self, num: int) -> str:
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        # Converting to roman
        thousands = m[num // 1000]
        hundreds = c[(num % 1000) // 100]
        tens = x[(num % 100) // 10]
        ones = i[num % 10]

        return (thousands + hundreds + tens + ones)


ss = Solution()
print(ss.intToRoman(150))
