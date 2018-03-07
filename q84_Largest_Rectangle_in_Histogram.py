class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        largest = {}
        currh = []

        for i, height in enumerate(heights):
            while currh and heights[currh[-1]] > height:
                currh.pop()

            for h in currh:
                largest[heights[h]][-1] += heights[h]

            if (not currh and height > 0) or (currh and height > heights[currh[-1]]):
                n = 1
                s = i - 1
                while s >= 0 and heights[i] <= heights[s]:
                    s -= 1
                    n += 1
                if height in largest:
                    largest[height].append(height * n)
                else:
                    largest[height] = [height * n]
                currh.append(i)
            pass

        newlist = [0]
        for m in list(largest.values()):
            newlist += m

        return max(newlist)

    def largestRectangleArea1(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        currh = []
        ans = 0

        for i, height in enumerate(heights):
            while currh and currh[-1][0] > height:
                ch,j = currh.pop()
                ans = max(ch*(i-j),ans)

            if (not currh and height > 0) or (currh and height > currh[-1][0]):
                s = i
                while s > 0 and heights[i] <= heights[s-1]:
                    s -= 1
                currh.append((height,s))
            pass
        i=len(heights)
        while currh:
            ch, j = currh.pop()
            ans = max(ch * (i - j), ans)

        return ans

s=[2,3,1]
print(Solution().largestRectangleArea1(s))
