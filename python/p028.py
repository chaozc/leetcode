class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            ans = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    ans = False
                    break
            if ans:
                return i
        return -1