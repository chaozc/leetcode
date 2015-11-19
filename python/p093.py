class Solution(object):
    def dfs(self, s, m):
        if m == 1:
            if int(s) < 256 and (s[0] != '0' or len(s) == 1):
                return [[s]]
            else:
                return []
        ans = []
        for i in range(3):
            if int(s[:i+1]) < 256 and (s[0] != '0' or i == 0) and len(s)-(i+1) <= 3*(m-1) and len(s)-(i+1) >= m-1 :
                tmp = self.dfs(s[i+1:], m-1)
                for it in tmp:
                    ans.append([s[:i+1]]+it)
        return ans
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        anss =  self.dfs(s, 4)
        return ['.'.join(it) for it in anss]