class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return 0 if ans>= 2147483648 or ans< -2147483648 else ans

    def reverse_m(self, x):
        ans = 0
        s = 1 if x>0 else -1
        x *=s
        while x != 0:
            ans = ans*10 + x % 10
            x //= 10
        ans *= s
        return 0 if ans>= 2147483648 or ans< -2147483648 else ans




s=Solution()
print(s.reverse_m(-13450))