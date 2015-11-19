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
                
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxh = Heap(cmp=lambda x, y:x>y)
        self.minh = Heap(cmp=lambda x, y:x<y)
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        self.maxh.push(num)
        if self.maxh.size() == self.minh.size()+2:
            x = self.maxh.pop()
            self.minh.push(x)
        if self.minh.size() > 0 and self.maxh.top() > self.minh.top():
            x, y = self.maxh.pop(), self.minh.pop()
            self.minh.push(x)
            self.maxh.push(y)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.maxh.size() == self.minh.size():
            return (self.maxh.top()+self.minh.top())*0.5
        else:
            return self.maxh.top()

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
print mf.findMedian()
mf.addNum(2)
print mf.findMedian()
mf.addNum(3)
print mf.findMedian()
mf.addNum(4)
print mf.findMedian()