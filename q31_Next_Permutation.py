class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        if i == 0:
            nums[:] = nums[::-1]
        else:
            j = i - 1
            k = i + 1
            while k < len(nums):
                if nums[k] < nums[i] and nums[k] > nums[j]:
                    i = k
                k += 1
            nums[j], nums[i] = nums[i], nums[j]
            nums[j + 1:] = sorted(nums[j + 1:])

    def nextPermutation2(self, nums):
        i = len(nums) - 1
        while i - 1 >= 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums[:] = nums[::-1]
            return
        else:
            j = i
            while j + 1 < len(nums) and nums[j + 1] > nums[i - 1]:
                j += 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            nums[i:] = nums[i:][::-1]
        return


s = Solution()
num = [2, 4, 1]
s.nextPermutation(num)
print(num)
