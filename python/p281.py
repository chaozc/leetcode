from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.d = [deque(v1), deque(v2)];
        if v1 != []:
            self.id = 0
        else:
            self.id = 1

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            ans = self.d[self.id].popleft()
            s = self.id
            self.id = (self.id+1)%2
            while self.id != s and len(self.d[self.id]) == 0:
                self.id = (self.id+1)%2
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.d[self.id]) != 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())