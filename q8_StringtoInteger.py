class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        try:
            s = str.strip()
            s = list(s)
            num, sign = 0, 1
            if s[0] == "-" or s[0] == "+":
                if s[0] == "-":
                    sign = -1
                del s[0]
            for c in s:
                if c.isdigit():
                    num = 10 * num + int(c)
                else:
                    break
            return min(2147483647, max(-2147483648, sign * num))
        except:
            return 0

    def myAtoi_RegEx(self, str):
        """
        :type str: str
        :rtype: int
        ^: start
        [+-]?: 1 or 0 [+-]
        \d+: any numbers
        """
        import re
        str = str.strip()
        try:
            str = re.search(r'^[+-]?\d+', str).group()
            n = int(''.join(str))
            return min(2147483647, max(-2147483648, n))
        except:
            return 0


s=Solution()
print(s.myAtoi_RegEx("+-342ewf"))



