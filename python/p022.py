class Solution(object):
    def dfs(self, l, r, n, st):
        if l == n and r == n:
            self.ans.append(st)
        if l < n:
            self.dfs(l+1, r, n, st+'(')
        if r < l:
            self.dfs(l, r+1, n, st+')')
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        self.dfs(0,0,n,'')
        return self.ans