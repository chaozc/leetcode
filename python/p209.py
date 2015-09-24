class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        ans = length+1
        left = 0
        right = -1
        sumn = 0
        while right < length-1:
        	right += 1
        	sumn += nums[right]
        	while (sumn >= s and right >= left):
        		ans = min(ans, right-left+1)
        		sumn -= nums[left]
        		left += 1
        if ans == length+1:
        	return 0
        else:
        	return ans

if __name__ == "__main__":
	a = Solution()
	print a.minSubArrayLen(100, [2,3,8,2,4,3])