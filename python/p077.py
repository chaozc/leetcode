class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        if k == 1:
            return [[i] for i in range(1, n+1)]
        ans = []
        for i in range(n, k-1, -1):
            tmp = self.combine(i-1, k-1)
            for it in tmp:
                ans.append(it+[i])
        return ans