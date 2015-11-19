class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ans = [[0 for i in range(n)]for j in range(m)]
        ans[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                else:
                    f1 = ans[i-1][j] if i > 0 else 0
                    f2 = ans[i][j-1] if j > 0 else 0
                    ans[i][j] += f1+f2
        return ans[-1][-1]