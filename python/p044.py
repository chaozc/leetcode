class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        tmp = p
        p = ""
        i = 0
        while i < len(tmp):
            p += tmp[i]
            if tmp[i] == '*':
                j = i+1
                while j < len(tmp) and tmp[j] == '*':
                    j += 1
                i = j
            else:
                i += 1
        print p
        if (p[0] == '?') or (p[0] == '*'):
            f = [True for i in range(len(s)+1)]
        else:
            f = [False for i in range(len(s)+1)]

        for i in range(1, len(p)):
            for j in range(len(s), 0, -1):
                if p[i] == '?':
                    f[j] = f[j-1]
                elif p[i] == '*':
                    for k in range(j-1, -1, -1):
                        f[j] = f[j] or f[k]
                        if f[j]:
                            break
                else:
                    f[j] = f[j-1] and (p[i] == s[j-1])
            f[0] = f[0] and ((p[i] == '?') or (p[i] == '*'))
        return f[-1]
a = Solution()
print a.isMatch("baabbabaaaabababbbabbaabbabbabbbbbbabaaaaababbbaababaaabaaaabbbaaaaaaaaaabbaaaaaaabaabbabaaabaaaaaabaabbbabbbbbbaabababbabbabaaaaabbaaabbbaaabbababaaabbbbbbbbbbbaabaaabbababaaaababbaabbbaaabbbbaabaaba",
"a*a*b*bb*ba***aab***b******aabaa*a*a*a*b**abbb***a*b*a*a*bb**ba****baa*****a*b***aaab*bab*****bb*a**")