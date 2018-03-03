class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def match(s, p):
            if p == '?':
                return True
            return p == s

        dict = {}
        for i in range(len(s) + 1):
            for j in range(len(p) + 1):
                if j == 0:
                    dict[i, j] = True if i == 0 else False
                elif p[j - 1] == '*':
                    dict[i, j] = False
                    for x in range(i + 1):
                        if dict[x, j - 1]:
                            dict[i, j] = True
                            break
                elif i == 0:
                    dict[i, j] = False
                else:
                    dict[i, j] = dict[i - 1, j - 1] and match(s[i - 1], p[j - 1])
        return dict[len(s), len(p)]

    def isMatch1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def match(s, p):
            if p == '?':
                return True
            return p == s

        dict = {}

        ns = 0
        for i in range(len(p)):
            if p[i]=='*':
                ns += 1
            elif ns == 0:
                if i>=len(s) or not match(s[i],p[i]):
                    return False
                else:
                    dict[i+1,i+1]=True

        if len(p)-ns>len(s):
            return False

        def dp(i, j):
            if (i, j) not in dict:
                if j == 0:
                    dict[i, j] = True if i == 0 else False
                elif p[j - 1] == '*':
                    dict[i, j] = False
                    for x in range(i+1):
                        if dp(x, j - 1):
                            dict[i, j] = True
                            break
                elif i == 0:
                    dict[i, j] = False
                else:
                    dict[i, j] = match(s[i - 1], p[j - 1]) and dp(i - 1, j - 1)
            return dict[i, j]

        return dp(len(s), len(p))

    def isMatch2(self, s, p):
        if not p:
            return not s

        m, n = len(s), len(p)
        i = j = 0
        last_x = 0
        last_y = -1
        while i < m:
            if j < n and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                last_x = i
                last_y = j
                j += 1
            elif last_y >= 0:
                i = last_x + 1
                j = last_y
            else:
                return False

        while j < n and p[j] == '*':
            j += 1

        return j == n

    def isMatch3(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def match(s, p):
            return p == s or p == '?'

        dict = {}
        def dp(i, j):
            if (i, j) not in dict:
                if j == 0:
                    dict[i, j] = True if i == 0 else False
                elif p[j - 1] == '*':
                    if i>0:
                        dict[i, j] = dp(i-1,j) or dp(i,j-1)
                    else:
                        dict[i,j] = dp(i,j-1)
                elif i == 0:
                    dict[i, j] = False
                else:
                    dict[i, j] = match(s[i - 1], p[j - 1]) and dp(i - 1, j - 1)
            return dict[i, j]

        return dp(len(s), len(p))


# s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# p="*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*"

# s="bbaaabaabbaaaabbbaaabbbaababbbbababbbbbabbabbaabaabbaabaabbbabaabbbbbabababbabaabbababbabbbbabbbbaaaaaaaabbaab"
# p="a**abaaa*b*aa*ba*****b*a*bb**bbab*a*aa**b***ba*a*aabb*bab**aa*ab*b**b*b*aabba******bbbb*aa*a****abb***b*"
s = 'aab'
p = 'c*a*b'
if __name__ == '__main__':
    print(Solution().isMatch3(s, p))

