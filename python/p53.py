#f[i] = max{f[i-1]+nums[i], nums[i]}
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        ans = nums[0]
        f = nums[0]
        for i in range(1, length):
        	f = max(f+nums[i], nums[i])
        	ans = max(f, ans)
        return ans
if __name__ == "__main__":
	a = Solution()
	print a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])