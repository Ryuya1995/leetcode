class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:].startswith(needle):
                return i
        return -1

        # or you can
        # return haystack.find(needle)
        # return haystack.index(needle)