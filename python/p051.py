class Solution(object):
    def dfs(self, n, row, col, d1, d2, posAtRow):
        
        if row == n:
            tmp = []
            for i in range(n):
                st = ""
                for j in range(posAtRow[i]):
                    st += "."
                st += "Q"
                for j in range(posAtRow[i]+1, n):
                    st += "."
                tmp.append(st)
            self.ans.append([it for it in tmp])
        else:
            #print row, posAtRow, col, d1, d2
            for j in range(n):
                #print j, col[j], d1[row+j], d2[row-j+n-1]
                if col[j] and d1[row+j] and d2[row-j+n-1]:
                    col[j] = False; d1[row+j] = False; d2[row-j+n-1] = False;
                    posAtRow[row] = j
                    self.dfs(n, row+1, col, d1, d2, posAtRow)
                    col[j] = True; d1[row+j] = True; d2[row-j+n-1] = True;
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.ans = []
        self.dfs(n, 0, [True for i in range(n)], [True for i in range(2*n-1)], [True for i in range(2*n-1)], [0 for i in range(n)])
        return self.ans
if __name__ == "__main__":
    a = Solution()
    print a.solveNQueens(8)