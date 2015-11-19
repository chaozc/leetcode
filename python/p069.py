class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return x
        l = 1; r = x
        while l < r:
            mid = (l+r)/2
            re = mid*mid
            if re == x:
                return mid
            elif re < x:
                if (mid+1)*(mid+1) <= x:
                    l = mid+1
                else:
                    return mid
            else:
                r = mid-1
        return l