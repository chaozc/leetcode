class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
        n = len(costs)
        k = len(costs[0])
        min1 = 0
        min2 = 0
        f = [0 for i in range(k)]
        for i in range(n):
            last_min1 = min1
            last_min2 = min2
            min1 = -1
            min2 = -1
            for j in range(k):
                if f[j] == last_min1:
                    f[j] = last_min2+costs[i][j]
                else:
                    f[j] = last_min1+costs[i][j]
                if min1 == -1 or min1 >= f[j]:
                    min2 = min1
                    min1 = f[j]
                elif min2 == -1 or min2 > f[j]:
                    min2 = f[j]
        return min1