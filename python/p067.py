class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            p = a; a = b; b = p;
        for i in range(len(a)-len(b)):
            b = "0"+b
        c = 0;
        st = ""
        for i in range(len(a)):
            j = len(a)-1-i
            t = int(a[j])+int(b[j])+c
            c = t/2
            st = str(t%2)+st
        if c == 1:
            st = "1"+st
        return st