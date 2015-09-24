#DFS
#Use f[i][j] to store whether s[i:j+1] is palindrome
class Solution(object):
    def check(self, s, l, r):
        if self.f[l][r] == 1:
            return True
        if self.f[l][r] == -1:
            return False
        if s[l] == s[r]:
            if l+1 <= r-1:
                if self.check(s, l+1, r-1):
                    self.f[l][r] = 1
                    return True
                else:
                    self.f[l][r] = -1
                    return False
            else:
                self.f[l][r] = 1
                return True
        else:
            self.f[l][r] = -1
            return False
    def search(self, s, l, r):
        ans = []
        if self.check(s, l, r):
            ans = [[s[l:r+1]]]
        for cut in range(l, r):
            if self.check(s, l, cut):
                ansr = self.search(s, cut+1, r)
                for ar in ansr:
                    ans.append([s[l:cut+1]]+ar)
        return ans
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        self.f = [[0 for i in range(n)]for j in range(n)]
        return self.search(s, 0, n-1)

        