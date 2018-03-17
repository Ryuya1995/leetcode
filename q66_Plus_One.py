class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        elif digits[-1] == 9:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
        else:
            digits[-1] += 1
        return digits

    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]
        if digits[-1] == 9:
            return self.plusOne(digits[:-1]) + [0]
        return digits[:-1] + [digits[-1]+1]

    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        ret = digits[:]  ## a[:] 和 a.copy()均为复制列表
        car = 1
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:  # 数值运算改为逻辑运算提升效率
                ret[i] += 1
                car = 0
                break
            else:
                ret[i] = 0

        if (car == 1):
            ret = [1] + ret

        return ret
