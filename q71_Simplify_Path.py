class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        rstr = []
        path = path.split('/')
        for x in path:
            if x == '..':
                if rstr:
                    rstr.pop()
            elif x == '.' or x == '':
                pass
            else:
                rstr.append(x)
        # if rstr:
        #     ans = ''
        #     for y in rstr:
        #         ans += '/' + y
        #     return ans
        # else:
        #     return '/'
        return '/' + '/'.join(rstr)
