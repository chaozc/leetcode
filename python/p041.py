#http://www.cnblogs.com/AnnieKim/archive/2013/04/21/3034631.html
#note the ans must be smaller than n
#swap the elements to let each one be the position they are supposed to be
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while (i < len(nums)):
            k = nums[i];
            if k > 0 and k < len(nums) and k-1 != i and nums[k-1] != k:
                nums[i] = nums[k-1]; nums[k-1] = k
            else:
                i = i+1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1