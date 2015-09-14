#f[k][i]: At most k transaction is allowed, f[k][i] is the maximum profit after day i
#f[1][i] = max(f[1][i-1], prices[i]-min) where min is the minimal price before day i
#f[k][i] = max{f[k][i-1], max{f[k-1][j]+price[i]-price[j+1]}where j < i}
#let g[k][i] = max{f[k-1][j]-price[j+1]} where j < i
#f2[i] = max(f2[k][i], g[k][i]+price[i])
#O(nk)

#PS. if k >> len(prices), then k is meaningless, we can treat this problem as p122.
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0 or k == 0:
        	return 0
        if k >= length:
        	f = 0
        	g = -prices[0]
	        for i in range(1, length):
	        	g = max(g, f-prices[i])
	        	f = prices[i]+g
	        return f
        else:
	        f = (k+1)*[0]
	        g = (k+1)*[-prices[0]]
	        mi = prices[0]
	        for i in range(1, length):
	        	mi = min(mi, prices[i])
	        	f[1] = max(f[1], prices[i]-mi)
	        	
	        	for kk in range(2, k+1):
	        		g[kk] = max(g[kk], f[kk-1]-prices[i])
	        		f[kk] = max(f[kk], g[kk]+prices[i])
	        	
	        	#print i, f1, g, f2
	        return f[k]

if __name__ == "__main__":
	a = Solution()
	print a.maxProfit(2, [2,1,4,5,2,9,7])