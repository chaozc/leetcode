#f[i][j]: the length of the longest '1's from point(i,j) to left
#leverage the algorithms in p084 on each column
#O(nm) the size of the matrix
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
        	return 0

        nx = len(matrix)
        ny = len(matrix[0])

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
        #print f
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
        				area = i*f[p][j]
        			else:
        				area = (i-pos[top]-1)*f[p][j]
        			#print i, pos[top], f[p][j]
        			ans = max(ans, area)
        			i -= 1
        return ans
if __name__ == "__main__":
	a = Solution()
	print a.maximalRectangle([['1']])