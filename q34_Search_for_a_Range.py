class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            if target > nums[r] or target < nums[l]:
                return [-1, -1]
            k = (r + l) // 2
            if nums[k] == target:
                tl = tr = k
                while tl - 1 >= 0 and nums[tl - 1] == target:
                    tl -= 1
                while tr + 1 < len(nums) and nums[tr + 1] == target:
                    tr += 1
                return [tl, tr]
            elif nums[k] > target:
                r = k
            else:
                l = k + 1
        if l == r and nums[l] == target:
            return [l, r]
        return [-1, -1]

    def searchRange1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums:
            left = 0
            right = len(nums) - 1
            if nums[left] > target or nums[right] < target:
                return [-1, -1]
            while left <= right:
                if left == right:
                    start = left
                    left += 1
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            left = 0
            right = len(nums) - 1
            while left <= right:
                if left == right:
                    end = right
                    right -= 1
                mid = (left + right) // 2 + 1
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            if start <= end:
                return [start, end]
            else:
                return [-1, -1]
        return [-1, -1]
