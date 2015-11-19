class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        f1 = 1
        f2 = 0
        for i in range(len(s)):
            f = 0
            if s[i] != '0':
                f += f1
            if i > 0 and s[i-1] != '0' and s[i-1:i+1] < '27':
                f += f2
            f2 = f1
            f1 = f
        return f