class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        flag = 0
        for _ in range(len(nums)):
            if nums[i] == target:
                if i < 0:
                    return i + len(nums)
                return i
            elif nums[i] < target:
                if flag == 1:
                    i += 1
                elif flag == 0:
                    flag = 1
                    i += 1
                elif flag == -1:
                    return -1
            else:
                if flag == -1:
                    i -= 1
                elif flag == 0:
                    flag = -1
                    i -= 1
                elif flag == 1:
                    return -1
        return -1

    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        if target in nums:
            res = nums.index(target)
        else:
            res = -1
        return res
