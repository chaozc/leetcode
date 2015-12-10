import Queue
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) > 0 and len(rooms[0]) > 0:
            INF = 2147483647
            n = len(rooms)
            m = len(rooms[0])
            q = Queue.Queue()
            for i in range(n):
                for j in range(m):
                    if rooms[i][j] == 0:
                        q.put((i,j))
            while not q.empty():
                pos = q.get()
                for dis in [(1,0),(-1,0),(0,1),(0,-1)]:
                    i = pos[0]+dis[0]
                    j = pos[1]+dis[1]
                    if i > -1 and i < n and j > -1 and j < m and rooms[i][j] == INF:
                        rooms[i][j] = rooms[pos[0]][pos[1]]+1
                        q.put((i,j))
                        