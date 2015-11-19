class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        base = 1
        c = [i+1 for i in range(n)]
        for i in range(n-1):
            base *= (i+1)
        ans = ''
        for i in range(n):
            p = (k-1)/base+1 ##
            k = k-base*(p-1) ##
            j = 0
            while p > 0:
                if c[j] > 0:
                    p -= 1
                j += 1
            ans += str(c[j-1])
            c[j-1] = 0
            
            if i < n-1:
                base /= (n-1-i)
        return ans