class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        left = []
        wid = []
        ans = 0
        for h in height:
            if not left:
                if h > 0:
                    left.append(h)
                    wid.append(1)
            elif h < left[-1]:
                left.append(h)
                wid.append(1)
            elif h == left[-1]:
                wid[-1] += 1
            else:  # h>left[-1]
                newwid = 1
                while left and h > left[-1]:
                    mid = left.pop()
                    width = wid.pop()
                    if left:
                        lefth = left[-1]
                        if lefth < h:
                            wid[-1] += width
                            ans += (lefth - mid) * width
                        elif lefth > h:
                            newwid = 1 + width
                            ans += (h - mid) * width
                        else:
                            ans += (h - mid) * width
                if left and left[-1]==h:
                    wid[-1]+=1+width
                else:
                    left.append(h)
                    wid.append(newwid)
        return ans

    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        result = 0
        while left<right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    result += left_max-height[left]
                left_max = max(left_max,height[left])
                left+=1
            else:
                if height[right] < right_max:
                    result += right_max-height[right]
                right_max = max(right_max,height[right])
                right-=1
        return result


height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height2 = [2,1,0,2]
height3 = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]

print(Solution().trap(height1))
print(Solution().trap(height2))
print(Solution().trap(height3))

