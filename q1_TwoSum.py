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
        for i in range(len(nums)):
            x=nums[i];y=target-x
            if y in hash:
                return [hash[y],i]
            else:
                hash[x]=i
        return "not found"


# p=Solution()
# nums=[2,4,6,8,9]
# print(p.twoSum(nums,10))
