#Scan from left to right
#for each position i, where nums[i] is not zero, record the # of 0s, say nzero, then i-nzero is the position nums[i] is supposed to be, swap the nums[i] and nums[i-nzero]
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nzero = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nzero += 1
            else:
                k = nums[i]; nums[i] = nums[i-nzero]; nums[i-nzero] = k;