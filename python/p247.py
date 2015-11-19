from collections import deque
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        elif n == 1:
            return ['0', '1', '8']
        elif n == 2:
            return ["11","69","88","96"]
        if n%2 == 0:
            d = deque(["00","11","69","88","96"])
            st = 4
        else:
            d = deque(['0', '1', '8'])
            st = 3
        for i in range(st, n+2, 2):
            m = len(d)
            for j in range(m):
                base = d.popleft()
                for pt in ["00","11","69","88","96"]:
                    d.append(pt[0]+base+pt[1])
        ans = []
        while len(d) > 0:
            c = d.popleft()
            if c[0] != '0':
                ans.append(c)
        return ans