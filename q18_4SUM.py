class Solution(object):
    def fourSum(self, nums, target=0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.nSum(sorted(nums), 4, [], target)

    def nSum(self, nums, N, pres, target):
        if len(nums) < N or N < 2:
            return list()
        res = []
        if N == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                sm = nums[left] + nums[right]
                if sm < target:
                    left += 1
                elif sm > target:
                    right -= 1
                else:
                    res.append(pres + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            return res
        for i in range(len(nums)):
            if target < nums[i] * N or target > nums[-1] * N:  # take advantages of sorted list
                break
            if i == 0 or nums[i] != nums[i - 1]:
                res += self.nSum(nums[i + 1:], N - 1, pres + [nums[i]], target - nums[i])
        return res

    # def fourSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """
    #     ans, i = [], 0
    #     nums.sort()
    #     while i < (len(nums) - 3):
    #         if nums[i] > target/4:
    #             break
    #         ans += self.threeSum(nums[i+1:], target - nums[i], nums[i])
    #         i += 1
    #         while i > 0 and i < len(nums) - 3 and nums[i] == nums[i - 1]:
    #             i += 1
    #     return ans
    #
    # def threeSum(self, nums, target, fourth):
    #     ans, i = [], 0
    #     # nums.sort()
    #     while i < (len(nums) - 2):
    #         if nums[i] > target/3:
    #             break
    #         j, k = i + 1, len(nums) - 1
    #         while j < k:
    #             s = nums[i] + nums[j] + nums[k]
    #             if s < target:
    #                 j += 1
    #             elif s > target:
    #                 k -= 1
    #             else:
    #                 ans.append([fourth, nums[i], nums[j], nums[k]])
    #                 k -= 1
    #                 j += 1
    #                 while j < k and nums[j] == nums[j - 1]:
    #                     j += 1
    #                 while j < k and nums[k] == nums[k + 1]:
    #                     k -= 1
    #         i += 1
    #         while i > 0 and i < len(nums) - 2 and nums[i] == nums[i - 1]:
    #             i += 1
    #     return ans



s=Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2,3,4,6,-3,5,6,78,53,23,1234,653,-32,-43,-32,-4,32,2,3,4,-3,-5,6,-7],1))