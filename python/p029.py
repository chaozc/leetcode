class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        i = 0
        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor
        i = 0
        
        d = divisor
        ans = 0
        while dividend >= d:
            i = 1
            while dividend >= d:
                d = d<<1
                i = i<<1
            i = i>>1
            d = d>>1
            ans += i
            dividend -= d
            d = divisor
            
            
        if sign > 0:
            if ans > 2147483647:
                ans -= 1
            return ans
        else:
            return -ans