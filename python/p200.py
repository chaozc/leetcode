from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        ans = 0
        dires = [(1,0), (0,1), (0,-1),(-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    d = deque([(i,j)])
                    grid[i][j] = 'v'
                    while len(d) > 0:
                        pos = d.popleft()
                        for dire in dires:
                            newpos = (pos[0]+dire[0], pos[1]+dire[1])
                            if newpos[0] > -1 and newpos[0] < len(grid) and newpos[1] > -1 and newpos[1] < len(grid[0]) and grid[newpos[0]][newpos[1]] == '1':
                                d.append(newpos)
                                grid[newpos[0]][newpos[1]] = 'v'
                    ans += 1
        return ans