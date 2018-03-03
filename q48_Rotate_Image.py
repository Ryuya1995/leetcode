class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        def swap(i1, j1):
            i2 = n - 1 - j1
            j2 = i1
            i3 = n - 1 - i1
            j3 = n - 1 - j1
            i4 = j1
            j4 = n - 1 - i1
            matrix[i1][j1], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4] = \
                matrix[i2][j2], matrix[i3][j3], matrix[i4][j4], matrix[i1][j1]

        n = len(matrix)
        # new_matrix = [[0 for _ in range(n)] for _ in range(n)]
        i = 0
        while i < n / 2:
            j = i
            while j < i + (n - i * 2) - 1:
                swap(i, j)
                j += 1
            i += 1

    def rotate1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])

    def rotate2(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i]=matrix[i][::-1]
        print(matrix)


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Solution().rotate2(matrix)
