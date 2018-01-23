class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        n = len(strs)
        if n < 1:
            return ans
        if n == 1:
            return strs[0]
        i = 0
        for i in range(len(strs[0])):
            x = strs[0][i]
            for j in strs[1:]:
                if i >= len(j):
                    return ans
                if x != j[i]:
                    return ans
            ans += x
        return ans


    def longestCommonPrefix_1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)

    def longestCommonPrefix_2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        pre = strs[0]
        for st in strs:
            while 1:
                if st.startswith(pre):
                    break
                else:
                    pre = pre[:-1]
        return pre
