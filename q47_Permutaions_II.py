class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]

        for n in nums:
            new_perm =[]
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perm.append(perm[:i]+[n]+perm[i:])
                    if i<len(perm) and n == perm[i]:
                        break
            perms = new_perm
        return perms

    def permuteUnique1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 0 : return res
        if len(nums) == 1 : return [nums]
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                #if [nums[i]]+j not in res:
                res.append([nums[i]]+j)
        return res



print(Solution().permuteUnique([ 1, 2,1]))