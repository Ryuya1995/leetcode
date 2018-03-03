class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = 0
        for i, j in enumerate(strs):
            while re.match("^" + j, s) != None: #s.startwith(j)
                ans += nums[i]
                s = s[len(j):]
            if s == "":
                return ans

    def romanToInt_1(self, s):
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        value = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                value -= roman[s[i]]
            else:
                value += roman[s[i]]
        value += roman[s[-1]]
        return value

s=Solution()
print(s.romanToInt_1("MMCLI"))