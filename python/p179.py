class Solution(object):
	def compare(self, x, y):
		if x+y < y+x:
			return 1
		return -1
	def largestNumber(self, nums):
		strs = [str(it) for it in nums]
		strs.sort(cmp=self.compare)
		ans = ''.join(strs)
		while len(ans) > 1 and ans[0] == '0':
			ans = ans[1:]
		return ans
if __name__ == "__main__":
	a = Solution()
	print a.largestNumber([0, 0])