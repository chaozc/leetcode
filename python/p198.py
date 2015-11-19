#dp
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) < 3:
            return max(nums)
            
        f = [0 if i > 1 else max(nums[:i+1]) for i in range(len(nums))]
        for i in range(2, len(nums)):
            f[i] = max(f[i-1], f[i-2]+nums[i])
        return f[-1]