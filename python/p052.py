class Solution(object):
    def dfs(self, n, row, col, d1, d2):
        if row == n:
            return 1
        else:
            tot = 0
            for j in range(n):
                if col[j] and d1[row+j] and d2[row-j+n-1]:
                    col[j] = False; d1[row+j] = False; d2[row-j+n-1] = False;
                    tot += self.dfs(n, row+1, col, d1, d2)
                    col[j] = True; d1[row+j] = True; d2[row-j+n-1] = True;
            return tot
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dfs(n, 0, [True for i in range(n)], [True for i in range(2*n-1)], [True for i in range(2*n-1)])