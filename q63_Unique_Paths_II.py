class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = {}
        rotateGrid = list(zip(*obstacleGrid))

        def path(m, n):
            if (m, n) in dp:
                return dp[m, n]
            if m == 0:
                if sum(obstacleGrid[m][0:n]) == 0:
                    dp[m, n] = 1
                else:
                    dp[m, n] = 0
            elif n == 0:
                if sum(rotateGrid[n][0:m]) == 0:
                    dp[m, n] = 1
                else:
                    dp[m, n] = 0
            else: #if m > 0 and n > 0
                if obstacleGrid[m][n] == 1:
                    dp[m,n]=0
                else:
                    dp[m, n] = path(m - 1, n) + path(m, n - 1)
            return dp[m, n]

        return path(m - 1, n - 1)

obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]