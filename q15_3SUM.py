class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans, i = [], 0
        nums.sort()
        while i < (len(nums) -2):
            if nums[i] > 0:
                break
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i > 0 and i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1
        return ans

    def threeSum_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        using Counter Class
        """
        from collections import Counter
        counter = Counter(nums)
        ans = [] if counter[0] < 3 else [[0, 0, 0]]

        ngs = sorted([x for x in counter if x < 0], reverse=True)
        n_ngs = sorted([x for x in counter if x >= 0])

        for n_ng in n_ngs:
            for ng in ngs:
                need = -(ng + n_ng)
                if need in counter:
                    if (need == ng or need == n_ng) and counter[need] > 1:
                        ans.append([ng, need, n_ng])
                    elif need < ng:
                        ans.append([need, ng, n_ng])
                    elif n_ng < need:
                        ans.append([ng, n_ng, need])
        return ans

s=Solution()
print(s.threeSum([0,0,0]))