class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        ans = 0
        while i < len(nums):
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            nums[ans] = nums[i]
            ans += 1
            i = j
        return ans