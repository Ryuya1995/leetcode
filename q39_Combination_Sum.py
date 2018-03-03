class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def Sum(candidates, target, pres=[]):
            res = []
            if candidates:
                x = candidates[0]
                if x == target:
                    res.append(pres+[x])
                elif x < target:
                    if x <= target/2:
                        res += Sum(candidates, target - x, pres + [x])
                    if len(candidates) > 1:
                        res += Sum(candidates[1:], target, pres)
            return res

        return Sum(sorted(candidates),target)


print(Solution().combinationSum([2, 3, 6, 7], 7))
