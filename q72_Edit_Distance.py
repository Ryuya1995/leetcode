class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = {}

        def edit(i, j):
            if (i, j) not in dp:
                if not (i and j):
                    dp[i, j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i, j] = edit(i - 1, j - 1)
                else:
                    dp[i, j] = min(edit(i - 1, j) + 1, edit(i, j - 1) + 1,
                                   edit(i - 1, j - 1) + 1)
            return dp[i, j]

        return edit(len(word1), len(word2))