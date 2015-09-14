#track the largest positive and negative sub-contigous series
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        po = 0
        ne = 0
        length = len(nums)
        ans = nums[0]
        for i in range(length):
        	if nums[i] == 0:
        		po = 0
        		ne = 0
        		ans = max(ans, 0)
        		continue
        	if nums[i] > 0:
        		if po > 0:
        			po *= nums[i]
        		else:
        			po = nums[i]
        		if ne < 0:
        			ne = ne*nums[i]
        		if po != 0:
        			ans = max(ans, po)
        		ans = max(ans, ne)
        	else:
        		p = po
        		if ne < 0:
        			po = ne*nums[i]
        		else:
        			ne = nums[i]
        			po = 0
        		if p > 0:
        			ne = p*nums[i]
        		else:
        			ne = nums[i]
        		if po != 0:
        			ans = max(ans, po)
        		ans = max(ans, ne)
        	#print po, ne
        return ans
if __name__ == "__main__":
	a = Solution()
	print a.maxProduct([7, -2, -4])