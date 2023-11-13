class Solution:
    def reverse(self, x: int) -> int:
        list_int = list(str(x))
        if list_int[0] == '-':
            list_reverse = ["-"]
            list_int.pop(0)
            list_reverse.extend(reversed(list_int))
            result = int(''.join(list_reverse))
        else:
            result = int(''.join(reversed(list_int)))
        if result > pow(2, 31) - 1 or result < pow(-2, 31):
            return 0
        return result


ss = Solution()
print(ss.reverse(120))
