class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        using a matrix to save every char in s with None to fill in the blanks
        then return the matrix without none
        """
        n = numRows
        sl = len(s)
        if sl<=n or n<2:
            return s
        a,b = divmod(sl,2*n-2)
        if b == 0:
            a, b = a - 1, b + 2 * n - 2
        maxy = (n - 1) * a + 1 if b <= n else (n - 1) * a + b % n + 1
        mat = [[None for i in range(maxy)] for i in range(n)]
        for i in range(sl):
            a, b = divmod(i+1, 2 * n - 2)
            if b == 0:
                a,b = a-1,b+2 * n - 2
            y = (n - 1) * a if b <= n else (n - 1) * a + b%n
            x = b - 1 if b < n else 2*n - b -1
            mat[x][y]=s[i]
        ans=""
        for i in range(n):
            for j in range(maxy):
                if mat[i][j]!= None:
                    ans += mat[i][j]
        return ans

    def convert2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        using a direct way to build the ans by some math calculate
        """
        n = numRows
        sl = len(s)
        if sl<=n or n<2:
            return s
        ans=""
        gap=2*(n-1)
        for i in range(n):
            tmp=i
            agap=2*n-2-2*i
            while(tmp<sl):
                ans+=s[tmp]
                if i!=0 and i!=n-1 and tmp+agap<sl:
                    ans+=s[tmp+agap]
                tmp+=gap
        return ans

    def convert3(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        very direct and simple way
        the point is to ignore the blank
        """
        step = (numRows==1) - 1
        ans=[""]*numRows
        idx=0
        for c in s:
            ans[idx] += c
            if idx==0 or idx==numRows-1:
                step = -step
            idx+=step
        return "".join(ans)



s=Solution()
print(s.convert3("abcdefegeew",4))