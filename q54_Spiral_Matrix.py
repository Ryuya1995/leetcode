class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        i,j=0,n-1
        spiral = matrix[0]
        direction = 1
        k = 1  # number of circle
        for _ in range((m - 1) * n):
            if direction == 0:  # right
                j += 1
                if j == n - k:
                    direction = 1
            elif direction == 1:  # down
                i += 1
                if i == m - k:
                    direction = 2
            elif direction == 2:  # left
                j -= 1
                if j == -1 + k:
                    direction = 3
            elif direction == 3:
                i -= 1
                if i == k:
                    direction = 0
                    k += 1
            spiral.append(matrix[i][j])
        return spiral

    def spiralOrder1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        spiral = matrix[0]
        i, j = 0, n - 1
        dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        d = 0
        k = n * (m - 1)
        while k > 0:
            for _ in range(m - 1):
                i += dirs[d][0]
                j += dirs[d][1]
                spiral.append(matrix[i][j])
                k -= 1
            m -= 1
            m, n = n, m
            d = (d + 1) % 4
        return spiral


matrix = [
    [13],
    [4],
    [7]
]
print(Solution().spiralOrder1(matrix))
