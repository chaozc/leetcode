class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        inc = True
        for i in range(len(nums)-1):
            if (inc and nums[i] > nums[i+1])or((not inc) and nums[i] <= nums[i+1]):
                k = nums[i]; nums[i] = nums[i+1]; nums[i+1] = k;
            inc = not inc