class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        tmpp = p
        p = ''
        while i < len(tmpp):
            p += tmpp[i]
            if tmpp[i] == '*':
                j = i
                while j < len(tmpp) and tmpp[j] == '*':
                    j += 1
                i = j
            else:
                i = i+1

        
        f = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        f[0][0] = True
        for i in range(len(s)+1):
            for j in range(1, len(p)+1):
                if i > 0 and p[j-1] != '*':
                    f[i][j] = (s[i-1] == p[j-1] or p[j-1] == '.') and f[i-1][j-1]
                elif p[j-1] == '*':
                    f[i][j] = f[i][j-1] or f[i][j-2] or (i > 0 and (p[j-2] == '.' or p[j-2] == s[i-1]) and f[i-1][j])
        return f[len(s)][len(p)]