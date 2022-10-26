class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        list_alphabet = "abcdefghijklmnopqrstuvwxyz"
        if len(list_alphabet) > len(sentence):
            return False
        list_alphabet = set(list_alphabet) - set(sentence)
        if len(list_alphabet) > 0:
            return False
        return True


ss = Solution()
print(ss.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
