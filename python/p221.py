#Sol1: Similar to p085, only differs at ***
#Sol2: dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+p(i,j)
class Solution(object):
    def maximalSquare(self, matrix):
    	
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
        	return 0

        nx = len(matrix)
        ny = len(matrix[0])
        #Sol 1
        """
        f = []
        for i in range(nx):
        	f.append([])
        	for j in range(ny):
        		if j == 0:
        			prev = 0
        		else:
        			prev = f[i][j-1]

        		if matrix[i][j] == '1':
        			f[i].append(prev+1)
        		else:
        			f[i].append(0)

        f.append([0]*ny)
        print f
        ans = 0
        for j in range(ny):
        	i = -1
        	pos = [0]*(nx+1)
        	top = -1
        	while i < nx:
        		i += 1
        		#print 'i', i
        		if top == -1 or f[i][j] >= f[pos[top]][j]:
        			top += 1
        			pos[top] = i
        		else:
        			p = pos[top]
        			top -= 1
        			if top == -1:
        				l = min(i, f[p][j])              #***#
        			else:
        				l = min((i-pos[top]-1),f[p][j]) #***#
        			#print i, pos[top], f[p][j]
        			ans = max(ans, l*l)
        			i -= 1
        """
        #Sol 2
        ans = 0
        dp = [[0]*ny for i in range(nx)]
        for i in range(nx):
        	for j in range(ny):
        		dp[i][j] = int(matrix[i][j])
        		if i and j and dp[i][j]:
        			dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
        		ans = max(ans, dp[i][j])
        return ans*ans
if __name__ == "__main__":
	a = Solution()
	print a.maximalSquare(["11","11"])