class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = s.split()
        if li == []:
            return 0
        else:
            return len(li[-1])