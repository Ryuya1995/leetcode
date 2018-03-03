class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        goal = len(nums)-1
        step = 0
        while i < goal:
            if i + nums[i]>= goal:
                return step + 1
            else:
                beststep = 1
                maxsum = 2
                for j in range(1,nums[i]+1):
                    sumstep = j + nums[i+j]
                    if sumstep > maxsum:
                        beststep = j
                        maxsum = sumstep
                i+=beststep
                step+=1
        return step

    def jump1(self,nums):
        lt=len(nums)-1
        mx=right=ct=0
        for i in range(lt):
            mx=max(i+nums[i],mx)
            if i==right:
                ct+=1
                right=mx
        return ct

nums = [2,3,1,1,4]
print(Solution().jump(nums))