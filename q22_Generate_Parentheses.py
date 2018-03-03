class Solution:
    def generateParenthesis(self, n, op=0):
        """
        :type n: int
        :rtype: List[str]
        recursively
        """
        if n > 0 and op >= 0:
            return ["(" + p for p in self.generateParenthesis(n - 1, op + 1)] + \
            [")" + p for p in self.generateParenthesis(n, op - 1)]
        return [")" * op] * (n == 0)

    def generateParenthesis_1(self, n):
        """
        :type n: int
        :rtype: List[str]
        iteratively
        """
        res = [[] for _ in range(n + 1)]
        res[0] += ['']
        for num in range(1, n + 1):
            for i in range(num):
                res[num] += ['(' + vi + ')' + vj for vi in res[i] for vj in res[num - 1 - i]]
        return res[n]

s=Solution()
print(s.generateParenthesis(4))





