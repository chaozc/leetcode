class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.v = []
        for l in vec2d:
            for it in l:
                self.v.append(it)
        self.n = len(self.v)
        self.i = -1

    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        return self.v[self.i]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < self.n-1

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())