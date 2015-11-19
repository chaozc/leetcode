class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = []
        base = []
        step = []
        exist = [False for i in range(n+1)]
        for i in range(1, n+1):
            if i*i < n:
                base.append(i*i)
                q.append(i*i)
                step.append(1)
                exist[i*i] == True
            elif i*i == n:
                return 1
            else:
                break
        length = len(base)
        l = -1
        while True:
            l += 1
            for i in range(length):
                new = q[l]+base[i]
                if new > n:
                    break
                elif exist[new]:
                    continue
                elif new < n:
                    q.append(new)
                    step.append(step[l]+1)
                    exist[new] = True
                elif new == n:
                    return step[l]+1