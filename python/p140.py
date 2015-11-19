class Solution(object):
    def dfs(self, n):
        if len(self.ans[n]) > 0:
            return
        for w in self.last[n]:
            if n+1 == len(w):
                self.ans[n].append(w)
            else:
                self.dfs(n-len(w))
                for pre in self.ans[n-len(w)]:
                    self.ans[n].append(pre+' '+w)
        return 
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        self.last = [[] for i in range(len(s))]
        for i in range(len(s)):
            for w in wordDict:
                if i-len(w)+1 < 0:
                    continue
                pt = s[i-len(w)+1:i+1]
                if pt == w and (i-len(w) == -1 or len(self.last[i-len(w)]) > 0):
                    self.last[i].append(w)
                    
        self.ans = [[] for i in range(len(s))]
        self.dfs(len(s)-1)
        return self.ans[-1]