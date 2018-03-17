class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        m = len(a)
        n = len(b)
        c = 0
        ans = []
        for i in range(n):
            c, div = divmod(int(a[-1-i]) + int(b[-1-i]) + c, 2)
            ans.append(div)
        for i in range(n, m):
            if c:
                c, div = divmod(int(a[-1-i]) + c, 2)
                ans.append(div)
            else:
                ans.append(a[-1-i])
        if c:
            ans.append(c)

        return ''.join(''.join(str(e) for e in ans[::-1]))

    def addBinary1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

print(Solution().addBinary("100","110010"))