class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        i = 0; j = len(num)-1;
        while i <= j:
            if not num[i]+num[j] in ['11','88','69','96', '00']:
                return False
            i += 1
            j -= 1
        return True