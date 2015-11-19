class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        f = [True for i in range(n)]
        ans = 0
        for i in range(2, n):
            if f[i]:
                ans += 1
                j = 2*i
                while j < n:
                    f[j] = False
                    j = j+i
        return ans