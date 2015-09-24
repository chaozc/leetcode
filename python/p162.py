#binary search
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums); l = 1; r = n-2;
        
        if n == 0:
            return None
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
            
        while l <= r:
            mid = (l+r)/2
            if (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1]):
                return mid
            elif nums[mid] < nums[mid-1] and nums[mid] > nums[mid+1]:
                r = mid-1
            elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                l = mid+1