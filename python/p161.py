class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "" and t == "":
            return False
        dif = abs(len(s)-len(t))
        if dif > 1:
            return False
        else:
            if len(s) > len(t):
                s, t = t, s
            
            i = 0
            while i < len(s) and s[i] == t[i]:
                i += 1
            if i < len(s):
                return s[i+1-dif:] == t[i+1:]
            else:
                return dif == 1