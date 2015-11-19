class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator%denominator == 0:
            return str(numerator/denominator)
        if numerator*denominator < 0:
            sign = "-"
        else:
            sign = ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        ans = str(numerator/denominator)+'.'
        n = numerator
        m = denominator
        r = n%m*10
        frac = ""
        appear = {}
        n = r*10
        while r > 0:
            if appear.has_key(r):
                frac = frac[:appear[r]]+'('+frac[appear[r]:]+')'
                break
            appear[r] = len(frac)
            frac += str(r/m)
            r = r%m*10
        ans += frac
        return sign+ans