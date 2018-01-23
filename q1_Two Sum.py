class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        One-pass Hash Table
        using the data structure dictionary
        """
        hash={}
        for i,x in enumerate(nums):
            if target-x in hash:
                return [hash[target-x],i]
            hash[x]=i


# p=Solution()
# nums=[2,4,6,8,9]
# print(p.twoSum(nums,10))
