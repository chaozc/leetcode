#Split to A1..Ai-1 and Ai+1...An and get two array of nums in O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        ans = [1]*length
        for i in range(1, length):
        	ans[i] = ans[i-1]*nums[i-1]
        p = 1
        for i in range(length-2, -1, -1):
        	p = p*nums[i+1]
        	ans[i] = p*ans[i]
        return ans
if __name__ == "__main__":
	a = Solution()
	print a.productExceptSelf([1,2,3,4])