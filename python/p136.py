class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for it in nums:
            if dic.pop(it, None) == None:
                dic[it] = 1
        return dic.keys()[0]