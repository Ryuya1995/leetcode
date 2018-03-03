import re


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            seq = ''
            i = 0
            j = 1
            for i in range(len(s)):
                if i + 1 < len(s) and s[i] == s[i + 1]:
                    j += 1
                else:
                    seq += str(j) + str(s[i])
                    j = 1
                s = seq
        return s

    def countAndSay2(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'

        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s
