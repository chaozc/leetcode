class Solution:
    # @return a string
    def countAndSay(self, n):
        ans = '1'
        for i in range(n-1):
            tmp = ''
            i = 0
            while i < len(ans):
                ch = ans[i]
                cnt = 0
                while i < len(ans) and ans[i] == ch:
                    cnt += 1
                    i += 1
                tmp += (str(cnt)+ch)
            ans = tmp
        return ans
        