class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]

    def permute1(self, nums):
        perms = [[]]
        for n in nums:
            newperms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    newperms.append(perm[:i] + [n] + perm[i:])
            perms = newperms
        return perms

    def permute2(self, nums):
        def backtrack(list,tempList,nums):
            if len(tempList)==len(nums):
                list.append(tempList.copy())
            else:
                for i in range(len(nums)):
                    if nums[i] in tempList:
                        continue
                    tempList.append(nums[i])
                    backtrack(list,tempList,nums)
                    tempList.pop()
        list = []
        backtrack(list,[],nums)
        return list



print(Solution().permute2([2, 3, 5]))
