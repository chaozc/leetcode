class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        base = 1
        while n != m:
            base *= 2
            n /= 2
            m /= 2
        return m*base