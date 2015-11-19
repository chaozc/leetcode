class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        elif n == 2:
            return k*k
        else:
            fnm1 = k-1
            fnm2 = 1
            for i in range(3, n+1):
                f = (k-1)*(fnm1+fnm2)
                fnm2 = fnm1
                fnm1 = f
            return k*(fnm1+fnm2)