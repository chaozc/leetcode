class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return x
        l = 1; r = x
        while l+1 < r:
            mid = (l+r)/2
            re = mid*mid
            if re <= x:
                l = mid
            else:
                r = mid-1
        if r*r <= x:
            return r
        else:
            return l