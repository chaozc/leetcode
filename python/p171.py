class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        n = len(s)
        ans = 0
        v = 1
        for i in range(n):
            ans += (ord(s[n-1-i])-ord('A')+1)*v
            v *= 26
        return ans