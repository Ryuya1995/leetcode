class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans, i = float('inf'), 0
        nums.sort()
        while i < (len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                ans = s if abs(target-s) < abs(target-ans) else ans
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return s
            i += 1
            while i > 0 and i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return ans

s = Solution()
print(s.threeSumClosest([-1,0,1,1,55],3))