class Solution(object):
    def dfs(self, target, num, last, result, st):
        if len(num) == 0:
            if target == result:
                self.ans.append(st)
            return
        for i in range(len(num)):
            if num[0] == '0' and i > 0:
                return
            n = int(num[:i+1])
            if len(st) > 0:
                self.dfs(target, num[i+1:], n, result+n, st+'+'+num[:i+1])
                self.dfs(target, num[i+1:], -n, result-n, st+'-'+num[:i+1])
                self.dfs(target, num[i+1:], last*n, result-last+last*n, st+'*'+num[:i+1])
            else:
                self.dfs(target, num[i+1:], n, n, num[:i+1])
                
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.ans = []
        self.dfs(target, num, 0, 0, '')
        return self.ans