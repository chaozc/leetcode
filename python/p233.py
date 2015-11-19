class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
           return 0 
        ndi = 0;
        m = n;
        while m > 0:
            ndi += 1
            m /= 10
        f = [0 for i in range(ndi+1)]
        f[1] = 1
        tens = 1
        for i in range(2, ndi+1):
            tens *= 10
            f[i] = 10*f[i-1]+tens

        ans = 0
        while n > 0:
            fd = n/tens
            n = n%tens
            ndi -= 1
            if fd == 1:
                ans += n+1
            else:
                if fd != 0:
                    ans += tens
            ans += fd*f[ndi]
            tens /= 10
        return ans