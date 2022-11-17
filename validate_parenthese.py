class Solution:
    def isValid(self, s: str) -> bool:
        check_list = []
        if len(s) % 2 != 0:
            return False
        for single_char in s:
            if single_char == "(" or single_char == "{" or single_char == "[":
                check_list.append(single_char)
            elif len(check_list) > 0:
                if single_char == ")" and check_list[-1] == "(":
                    check_list = check_list[:-1]
                elif single_char == "}" and check_list[-1] == "{":
                    check_list = check_list[:-1]
                elif single_char == "]" and check_list[-1] == "[":
                    check_list = check_list[:-1]
                else:
                    return False
            else:
                return False
        if len(check_list) > 0:
            return False
        return True


ss = Solution()
print(ss.isValid("{}}[]()"))
