#binary search
#case1: left part increasing num[l] <= num[mid]-> pivot at right
#case2: pivot at left
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
        	mid = (l+r)/2
        	if nums[mid] == target:
        		return mid
        	if nums[mid] >= nums[l]:
        		if nums[l] <= target and target <= nums[mid]:
        			r = mid-1
        		else:
        			l = mid+1
        	else:
        		if nums[mid] >= target or target >= nums[l]:
        			r = mid-1
        		else:
        			l = mid+1
        return -1
if __name__ == "__main__":
	a = Solution()
	print a.search([4,5,6,7,0,1,2], 0)