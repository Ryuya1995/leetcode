class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        return re.match(p + '$', s) != None

    def isMatch_dic(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        using dynamic programming
        dict is to save the result of whether i of s and j of p is matched
        """
        dict={}
        for i in range(len(s)+1):
            for j in range(len(p)+1):
                if j==0:
                    dict[i,j] = (i == 0)
                elif j>1 and p[j-1] == "*":
                    dict[i,j] = dict[i,j-2] or (i>0 and (p[j-2] == "." or p[j-2] == s[i-1]) and (dict[i-1,j] or dict[i,j-1]))
                else:
                    dict[i,j] = i>0 and dict[i-1,j-1] and (p[j-1] == "." or p[j-1] == s[i-1])
        return dict[len(s),len(p)]

    def isMatch_dp(self, text, pattern):
        #using dynamic programming and recursion
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)




s=Solution()
print(s.isMatch("fe", "fe*"))
print(s.isMatch_dp("aaa", "ab*a*c*a"))
