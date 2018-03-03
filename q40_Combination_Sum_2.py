class Solution:
    def combinationSum2(self, candidates, target):
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
                        res += Sum(candidates[1:], target - x, pres + [x])
                    while len(candidates) > 1 and candidates[1]==x:
                        candidates.pop(0)
                    if len(candidates) > 1:
                        res += Sum(candidates[1:], target, pres)
            return res

        return Sum(sorted(candidates),target)


print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
