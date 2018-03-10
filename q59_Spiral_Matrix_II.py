class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        matrix[0] = list(range(1,n+1))
        i, j = 0, n - 1
        dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        d = 0
        m = n
        k = n + 1
        nn = n*n
        while k <= nn:
            for _ in range(m - 1):
                i += dirs[d][0]
                j += dirs[d][1]
                matrix[i][j] = k
                k += 1
            m -= 1
            m, n = n, m
            d = (d + 1) % 4
        return matrix

print(Solution().generateMatrix(3))


