# find the minimal price till now, update ans by (nums[i]-min) i.e sells at day i
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
        	return 0
        ans = 0;
        mi = prices[0]
        for i in range(1, length):
            mi = min(mi, prices[i])
            ans = max(ans, prices[i]-mi)
        return ans
if __name__ == "__main__":
	a = Solution()
	print a.maxProfit([])