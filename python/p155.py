#min[i]: the minimal number from stack[0] to stack[i]
#when push, min[i] = min(stack[i], min[i-1])
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.len = 0
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self.stack) == self.len:
            self.stack.append(x)
            self.min.append(x)
        
        self.len += 1
        self.stack[self.len-1] = x
        if self.len > 1:
            self.min[self.len-1] = min(x, self.min[self.len-2])
        else:
            self.min[self.len-1] = x
        #print self.min
        return

    def pop(self):
        """
        :rtype: nothing
        """
        if self.len > 0:
            self.len -= 1
        return

    def top(self):
        """
        :rtype: int
        """
        if self.len > 0:
            return self.stack[self.len-1]
        else:
            return
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.len > 0:
            return self.min[self.len-1]
        else:
            return

if __name__ == "__main__":
    a = MinStack()
    a.push(-2)
    a.push(0)
    a.push(-1)
    print a.getMin()