#binary search
#case1: left part increasing num[l] < num[mid]-> pivot at right
#case2: num[l] > num[mid] -> pivot at left
#case3: num[l] == num[mid], not sure, l=l+1
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums)-1
        while l <= r:
        	mid = (l+r)/2
        	if nums[mid] == target:
        		return True
        	if nums[l] < nums[mid]:
        		if nums[l] <= target and target <= nums[mid]:
        			r = mid-1
        		else:
        			l = mid+1
        	elif nums[l] > nums[mid]:
        		if target >= nums[l] or target <= nums[mid]:
        			r = mid-1
        		else:
        			l = mid+1
        	else:
        		l += 1
        return False
if __name__ == "__main__":
	a = Solution()
	print a.search([1,3,1,1,1], 3)