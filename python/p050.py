class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1/self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n%2 == 0:
            k = self.myPow(x, n/2)
            return k*k
        else:
            k1 = self.myPow(x, n/2)
            k2 = self.myPow(x, n-n/2)
            return k1*k2