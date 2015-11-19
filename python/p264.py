class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q2 = [2]; q3 = [3]; q5 = [5];
        if n == 1:
            return 1
        i2 = 0; i3 = 0; i5 = 0;
        for i in range(n-1):
            f2 = q2[i2]
            f3 = q3[i3]
            f5 = q5[i5]
            f = min(f2, f3, f5)
            q2.append(f*2)
            q3.append(f*3)
            q5.append(f*5)
            if f2 == f:
                i2 += 1
            if f3 == f:
                i3 += 1
            if f5 == f:
                i5 += 1
        return f
            