class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        h = len(triangle)
        if h == 0:
        	return 0
        dp = [[0]*(i+1) for i in range(h)]

        for i in range(h-1, -1, -1):
        	for j in range(i+1):
        		dp[i][j] = triangle[i][j]
        		if h-1-i:
        			dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        		
        return dp[0][0]
if __name__ == "__main__":
	a = Solution()
	print a.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])