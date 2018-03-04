class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def try_solve(guess, i):
            if 0 <= i < n:
                dia = []
                for x in range(i):
                    dia += [x + guess[x] - i, -x + guess[x] + i]
                possible = n_list - set(guess) - set(dia)
                if possible:
                    for j in possible:
                        guess[i] = j
                        if i == n - 1:
                            ans[0] += 1
                        else:
                            try_solve(guess.copy(), i + 1)
                else:
                    return

        ans = [0]
        n_list = set(range(n))
        try_solve([-1] * n, 0)

        return ans[0]