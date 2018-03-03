class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = []
        maxv = 0
        v = [(-1, -2)]
        for j, pt in enumerate(s):
            if pt == '(':
                left.append(j)
            if pt == ')' and left:
                l = left.pop()
                r = j
                (pl, pr) = v[-1]
                if r > pr and l < pl:
                    v.pop()
                if l == v[-1][1] + 1:
                    l=v[-1][0]
                    v.pop()
                    v.append((l, r))
                else:
                    v.append((l, r))
                maxv = max(maxv,v[-1][1]-v[-1][0]+1)
        return maxv

    def longestValidParentheses1(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]*len(s)
        left = 0
        ans = 0
        for i in range(0, len(s)):
            if s[i] == "(":
                left += 1
            elif left > 0:
                left -= 1
                dp[i] = dp[i-1] + 2
                j = i - dp[i]
                if j >= 0:
                    dp[i] += dp[j]
                ans = max(ans, dp[i])
        return ans

s = Solution()
print(s.longestValidParentheses1('()()()(())((()'))

