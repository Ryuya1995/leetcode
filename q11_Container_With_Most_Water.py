class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i, j = 0, len(height)-1
        maxArea = min(height[i], height[j]) * (j - i)
        while j > i+1:
            h1, h2 = height[i], height[j]
            if h1 > h2:
                j -= 1
                while j > i and h2 > height[j]:
                    j -= 1
            else:
                i += 1
                while j > i and h1 > height[i]:
                    i += 1
            maxArea = max(min(height[i], height[j]) * (j - i), maxArea)
        return maxArea

s=Solution()
print(s.maxArea([1,3,2,5,25,24,5]))