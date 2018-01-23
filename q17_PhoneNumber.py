class Solution:
    dictionary = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        recursion
        """
        if digits == "":
            return []
        if len(digits) == 1:
            return list(self.dictionary[digits[0]])
        base = self.letterCombinations(digits[:-1])
        add = list(self.dictionary[digits[-1]])
        return [b + a for b in base for a in add]

    def letterCombinations_1(self, digits):
        #Simplest is best
        return [b + a for b in self.dictionary.get(digits[:1],"") for a in self.letterCombinations(digits[1:]) or ['']] or []

s=Solution()
print(s.letterCombinations_1("324"))