class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l < r:
            k = (l+r)//2
            if nums[k] == target:
                return k
            elif nums[k]>target:
                r = k
            else:
                l = k+1
        if l == r and nums[l]<target:
            return l+1
        return l