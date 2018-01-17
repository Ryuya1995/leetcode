class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=sorted(nums1+nums2)
        if len(nums)%2:
            return nums[(len(nums)-1)//2]
        else:
            return (nums[len(nums)//2]+nums[len(nums)//2-1])/2


nums1 = [1, 2]
nums2 = [3,2,4]
n=Solution()
print(n.findMedianSortedArrays(nums1,nums2))