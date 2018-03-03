class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        ans = [0 for _ in range(n1 + n2)]
        rstr = ''
        for i in range(n1):
            for j in range(n2):
                x = int(num1[-1 - i])
                y = int(num2[-1 - j])
                c = x * y
                ans[i + j] += c % 10
                ans[i + j + 1] += c // 10
                if ans[i + j] > 9:
                    ans[i + j] = ans[i + j] % 10
                    ans[i + j + 1] += 1
                if ans[i+j+1]>9:
                    ans[i+j+1]=ans[i+j+1]%10
                    ans[i+j+2]+=1
        ans = ans[::-1]
        while ans and ans[0] == 0:
            ans.pop(0)
        if not ans:
            return '0'
        for x in ans:
            rstr += str(x)
        return rstr

    def multiply1(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        ans = [0]*(n1+n2)
        rstr = ''
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                x = int(num1[i])
                y = int(num2[j])
                c = x * y + ans[i + j+1]
                ans[i + j] += c // 10
                ans[i + j + 1] = c % 10
        for p in ans:
            if not (not rstr and p == 0):
                rstr+=str(p)
        return rstr if rstr else '0'

    def multiply2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1)*int(num2))

print(Solution().multiply('123456789', '987654321'))
print(Solution().multiply1('1', '987654321'))
