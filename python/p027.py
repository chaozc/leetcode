class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        nval = 0
        for i in range(n):
            if nums[i] == val:
                nval += 1
            else:
                k = nums[i]; nums[i] = nums[i-nval]; nums[i-nval] = k;
        return n-nval