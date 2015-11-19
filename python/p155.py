#min[i]: the minimal number from stack[0] to stack[i]
#when push, min[i] = min(stack[i], min[i-1])
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        else:
            self.min.append(min(self.min[-1], x))
        return

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()
        self.min.pop()
        return

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min) > 0:
            return self.min[-1]
        else:
            return