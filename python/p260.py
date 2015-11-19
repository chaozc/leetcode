class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for i in nums:
            xor ^= i
        lowbit = 1
        while xor%2 == 0:
            xor /= 2
            lowbit *= 2
        a = 0
        b = 0
        for i in nums:
            if lowbit & i:
                a ^= i
            else:
                b ^= i
        return [a,b]