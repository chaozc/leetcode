#dp:http://www.acmerblog.com/palindrome-partitioning-ii-6148.html
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        isPal = [[False for i in range(n)]for j in range(n)]
        cut = []
        for i in range(n):
            cut.append(i)
            for j in range(i+1):
                if (s[i] == s[j] and (i-j <= 1 or isPal[j+1][i-1])):
                    isPal[j][i] = True
                    if j > 0:
                        cut[i] = min(cut[i], cut[j-1]+1)
                    else:
                        cut[i] = 0
        return cut[n-1]
if __name__ == "__main__":
    a = Solution()
    print a.minCut("dde")
