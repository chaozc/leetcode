#f[i]: the max profit after day i
#f[i] = max{f[i-1], max{f[j]+price[i]-price[j+1]}(j < i)}
#Let g[i] = max{f[j]-price[j+1]}(j < i)
#So f[i] = max(price[i]+g[i], f[i-1]) =price[i]+g[i] 
#O(n)

#another solution: if price[i]<price[i+1] then ans+= price[i+1]-price[i]
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
        	return 0
        f = 0
        g = -prices[0]
        for i in range(1, length):
        	g = max(g, f-prices[i])
        	f = prices[i]+g
        return f
if __name__ == "__main__":
	a = Solution()
	print a.maxProfit([2,7,1,2])