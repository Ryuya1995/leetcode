class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        l = i = 0
        for j in range(len(s)):
            if s[j] in used and i<used[s[j]]:
                i = used[s[j]]
            l = max(l,j-i+1)
            used[s[j]] = j+1
        return l

# t = Solution()
# s = "abcabcbb"
# print(t.lengthOfLongestSubstring(s))

# l = 0
# for i in range(len(s)):
#     d = set()
#     for j in range(i,len(s)):
#         if s[j] in d:
#             if j-i>l:
#                 l=j-i
#             break
#         elif j==len(s)-1:
#             if j-i+1>l:
#                 l=j-i+1
#         else:
#             d.add(s[j])
# return l

# used = {}
# max_length = start = 0
# for i, c in enumerate(s):
#     if c in used and start <= used[c]:
#         start = used[c] + 1
#     else:
#         max_length = max(max_length, i - start + 1)
#
#     used[c] = i
#
# return max_length

