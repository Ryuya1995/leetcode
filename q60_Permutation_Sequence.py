import math


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        def inserti(self, i, j):  # insert self[i] to j
            self[j], self[j + 1:i + 1] = self[i], self[j:i]

        n_list = list(range(1, n + 1))
        x = [1]
        y = [0] * n
        for i in range(2, n + 1):
            x.append(i * x[-1])

        j = n - 1
        k = k - 1
        while k > 0:
            if k >= x[j]:
                k -= x[j]
                y[j] += 1
            else:
                j -= 1

        i = n - 1
        while i >= 0:
            if y[i] > 0:
                inserti(n_list, n - i - 2 + y[i], n - i - 2)
            i -= 1

        return ''.join(str(e) for e in n_list)

    def getPermutation1(self, n, k):
        li = [i for i in range(1, n + 1)]
        res = ''
        m = 1
        for i in range(1, n):
            m *= i
        for i in range(n, 0, -1):
            l = (k - 1) // m
            res += str(li[l])
            del li[l]
            k -= l * m
            if i > 1:
                m //= (i - 1)
        return res

    def getPermutation2(self, n, k):
        array = list(range(1, n + 1))
        k = (k % math.factorial(n)) - 1
        permutation = []
        for i in range(n - 1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            permutation.append(array.pop(idx))

        return "".join(map(str, permutation))


print(Solution().getPermutation2(3, 5))
