#f1[i]: if only one transaction is allowed, f1[i] is the maximum profit after day i
#f2[i]: At most two transaction is allowed, f2[i] is the maximum profit after day i
#f1[i] = max(f1, prices[i]-min) where min is the minimal price before day i
#f2[i] = max{f2[i-1], max{f1[j]+price[i]-price[j+1]}where j < i}
#let g[i] = max{f1[j]-price[j+1]} where j < i
#f2[i] = max(f2[i], g[i]+price[i])
#O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
        	return 0
        f1 = 0
        g = -prices[0]
        f2 = 0
        mi = prices[0]
        for i in range(1, length):
        	mi = min(mi, prices[i])
        	f1 = max(f1, prices[i]-mi)
        	
        	g = max(g, f1-prices[i])

        	f2 = max(f2, g+prices[i])
        	
        	#print i, f1, g, f2
        return f2

if __name__ == "__main__":
	a = Solution()
	print a.maxProfit([2,1,4,5,2,9,7])