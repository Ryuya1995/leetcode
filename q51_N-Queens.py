class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        give one solution
        """

        def insert_q(i):
            if i not in possible:
                dia = []
                for x, y in guess.items():
                    dia += [x + y - i, -x + y + i]
                possible[i] = nlist - set(list(guess.values())) - set(dia)
            for j in possible[i]:
                guess[i] = j
                sol[i] = '.' * j + 'Q' + '.' * (n - 1 - j)
                return True
            return False

        def try_solve():
            i = 0
            while i < n:
                if i < 0:
                    return False
                if not insert_q(i):
                    del possible[i]
                    i -= 1
                    if i < 0:
                        return False
                    j = guess[i]
                    sol[i] = '.' * n
                    possible[i].remove(j)
                    del guess[i]
                else:
                    i += 1
            return True

        sol = ['' for _ in range(n)]
        guess = {}
        possible = {}
        nlist = set(range(n))

        if try_solve():
            return sol
        else:
            return []

    def solveNQueens1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        give all solutions
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
                            ans.append(['.' * j + 'Q' + '.' * (n - 1 - j) for j in guess])
                        else:
                            try_solve(guess.copy(), i + 1)
                else:
                    return

        ans = []
        n_list = set(range(n))
        try_solve([-1] * n, 0)
        return ans

    def solveNQueens2(self, n):
        results = []
        sol = [0] * n
        rows_av = [True] * n
        diag1_av = [True] * (2 * n - 1)
        diag2_av = [True] * (2 * n - 1)

        def printSol():
            results.append(["." * i + "Q" + "." * (n - i - 1) for i in sol])

        def util(start):
            if start >= n:
                results.append(["." * i + "Q" + "." * (n - i - 1) for i in sol])
                return
            for j in range(n):
                if rows_av[j] and diag1_av[n - 1 + start - j] and diag2_av[start + j]:
                    sol[start] = j
                    rows_av[j] = diag1_av[n - 1 + start - j] = diag2_av[start + j] = False
                    util(start + 1)
                    rows_av[j] = diag1_av[n - 1 + start - j] = diag2_av[start + j] = True

        util(0)
        return results


print(Solution().solveNQueens1(5))
