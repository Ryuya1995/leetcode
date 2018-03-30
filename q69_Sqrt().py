class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sqr = 1
        div = x
        while round(div) != round(sqr):
            sqr = (div+sqr)/2
            div = x/sqr
        return round(sqr)

    def mySqrt1(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 1000
        while r**2>x or (r+1)**2<x:
            r = r/2+x/2/r
            r = int(r)
        return r
