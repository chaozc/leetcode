class Solution(object):
    def dfs(self, board, word, l, i, j, n, m):
        if l == len(word):
            return True
        for dis in [[1,0],[-1,0],[0,1],[0,-1]]:
            ii = i+dis[0]
            jj = j+dis[1]
            if ii >= 0 and ii < n and jj >= 0 and jj < m and self.visited[ii][jj] == False and board[ii][jj] == word[l]:
                self.visited[ii][jj] = True
                if self.dfs(board, word, l+1, ii, jj, n, m):
                    return True
                self.visited[ii][jj] = False
        return False
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        if len(board) == 0 or len(board[0]) == 0 or len(word) == 0:
            return False
        n = len(board);
        m = len(board[0]);
        self.visited = [[False for i in range(m)] for j in  range(n)];
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    self.visited[i][j] = True
                    if self.dfs(board, word, 1, i, j, n, m):
                        return True
                    self.visited[i][j] = False
        return False