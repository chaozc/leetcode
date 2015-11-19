class Heap:
    def __init__(self, cmp):
        self.cmp = cmp
        self.data = []

    def push(self, x):
        self.data.append(x)
        self.siftup(len(self.data)-1)

    def size(self):
        return len(self.data)

    def top(self):
        return self.data[0]

    def pop(self):
        if len(self.data) == 0:
            return None
        ans = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.siftdown(0)
        return ans

    def siftup(self, id):
        while id > 0 and self.cmp(self.data[id], self.data[(id-1)/2]):
            self.data[id], self.data[(id-1)/2] = self.data[(id-1)/2], self.data[id]
            id = (id-1)/2

    def siftdown(self, id):
        while id*2+1 < len(self.data):
            if id*2+2 < len(self.data) and self.cmp(self.data[id*2+2], self.data[id*2+1]):
                nid = id*2+2
            else:
                nid = id*2+1
            if self.cmp(self.data[nid], self.data[id]):
                self.data[id], self.data[nid] = self.data[nid], self.data[id]
                id = nid
            else:
                break
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        edges = []
        for i in range(len(buildings)):
            edges.append((i, -1, buildings[i][0], buildings[i][2]));
            edges.append((i, 1, buildings[i][1], buildings[i][2]));
        finish = [False for _ in buildings]
        edges.sort(key=lambda x:(x[2],x[1],x[1]*x[3]))
        h = Heap(cmp=lambda x,y:x[3]>y[3])
        last = 0
        ans = []
        #print edges
        for i in range(len(edges)):
            if edges[i][1] == -1:
                h.push(edges[i])
            else:
                finish[edges[i][0]] = True
                while (h.size()>0) and finish[h.top()[0]]:
                    h.pop()
            if h.size() == 0:
                now = 0
            else:
                now = h.top()[3]
            if now != last:
                ans.append([edges[i][2],now])
                last = now
        return ans
        