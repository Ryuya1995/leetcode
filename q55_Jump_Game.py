class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = len(nums) - 1
        k = 1
        while i > 0:
            j = i-k
            if nums[j] < k:
                if j > 0:
                    k += 1
                else:
                    return False
            else:
                i = j
                k = 1
        return True

    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        right:the right boundary
        mx:new right for a new i
        if right==i==mx then return false
        """
        lt=len(nums)-1
        mx=right=0
        for i in range(lt):
            mx=max(i+nums[i],mx)
            if i==right:
                if right==mx:
                    return False
            right=mx
        return True

    def canJump2(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True


