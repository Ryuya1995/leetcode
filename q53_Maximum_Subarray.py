class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums:
        #     left = 0
        #     right = len(nums)
        #     ans = nums[0]
        #     while left<right-1:
        #         ans = max(ans,sum(nums[left:right]))
        #         if nums[left]<=nums[right-1]:
        #             left+=1
        #         else:
        #             right-=1

        max_ending_here = max_so_far = nums[0]
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


print(Solution().maxSubArray([-5,8,-5,1,1,-3,5,5,-3,-3,6,4,-7,-4,-8,0,-1,-6]))