import math

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 2 or n < 2:
            return min(m,n)
        dp = {}
        def path(m, n):
            if (m,n) in dp:
                return dp[m,n]
            if m == 2 or n == 2:
                dp[m,n]= max(m,n)
            if m > 2 and n > 2:
                dp[m,n]= path(m - 1, n) + path(m, n - 1)
            return dp[m,n]

        return path(m,n)

    def uniquePaths1(self, m, n):
        if m < 2 or n < 2:
            return min(m,n)
        def path(m, n):
            if m == 2 or n == 2:
                res[0] += max(m,n)
                return
            if m > 1:
                path(m - 1, n)
            if n > 1:
                path(m, n - 1)
        res = [0]
        path(m, n)
        return res[0]

    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        N = n + m - 2;// how much steps we need to do
        k = m - 1; // number of steps that need to go down
        Combination(N, k) = n! / (k!(n - k)!)
        """
        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))

    def uniquePaths3(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def comb(a, b):
            stop = a - b
            res = 1
            while a != stop:
                res *= a
                a -= 1

            while b != 0:
                res //= b
                b -= 1

            return res

        return comb(m + n - 2, n - 1)


for n in range(2,10):
    for m in range(2,10):
        print(n, m, Solution().uniquePaths1(n, m),Solution().uniquePaths(n, m))
