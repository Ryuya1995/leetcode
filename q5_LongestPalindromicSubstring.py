class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ml = 0 #maxLength
        start = 0
        for i in range(n):
            if i-ml>0 and s[i-ml-1:i+1]==s[i-ml-1:i+1][::-1]: #for odd situation
                start=i-ml-1
                ml+=2
                continue
            if i-ml>-1 and s[i-ml:i+1]==s[i-ml:i+1][::-1]: #for even situation
                start=i-ml
                ml+=1
        return s[start:start+ml]

s=Solution()
print(s.longestPalindrome("jabcbafegefa"))

# n = len(s)
# ans = ""
# ml = 0
# for i in range(n):
#     j = 0
#     while i - j > -1 and i + j < n:
#         if s[i - j] == s[i + j]:
#             if j * 2 + 1 > ml:
#                 ml = j * 2 + 1
#                 ans = s[i - j:i + j + 1]
#             j += 1
#         else:
#             break
#     j = 0
#     while i - j > -1 and i + j + 1 < n:
#         if s[i - j] == s[i + j + 1]:
#             if j * 2 + 2 > ml:
#                 ml = j * 2 + 2
#                 ans = s[i - j:i + j + 2]
#             j += 1
#         else:
#             break
# return ans


