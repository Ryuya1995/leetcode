class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positives = [i for i in range(1, len(nums) + 2)]
        for x in nums:
            if x in positives:
                positives.remove(x)
        return positives[0]

    def firstMissingPositive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time
        our_set = set(nums)

        for i in range(1, len(our_set) + 2):
            if i not in our_set:
                return i
        # if empty
        return 1

    def firstMissingPositive2(self, nums):
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
            else:
                i += 1
        for j, x in enumerate(nums):
            if j + 1 != x:
                return j + 1
        return 1 + len(nums)


print(Solution().firstMissingPositive2([]))