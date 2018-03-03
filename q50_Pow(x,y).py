class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n > 0:
            if n%2:
                return x*self.myPow(x*x,n//2)
            return self.myPow(x*x,n/2)
        return 1/self.myPow(x,-n)

print(Solution().myPow(2.0,10))