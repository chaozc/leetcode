class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        c = 0
        digits[n-1] += 1
        for i in range(n-1, -1, -1):
            digits[i] += c
            c = digits[i]/10
            digits[i] %= 10
        if c == 1:
            digits = [1]+digits
        return digits