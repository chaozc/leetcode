class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        for k in [2, 3, 5]:
            while num % k == 0:
                num /= k
        if num == 1:
            return True
        else:
            return False