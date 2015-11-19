#for rotated sorted problem:binary search
#suppose minimal in nums[l->r]
#if n[l] < n[r] -> return n[l]
#else check n[mid]
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0; r = len(nums)-1
        while l <= r:
            if nums[l] < nums[r] or l == r:
                return nums[l]
            mid = (l+r)/2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1