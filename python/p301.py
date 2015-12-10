import Queue
from sets import Set
class Solution(object):
    def isvalid(self, s):
        l = 0
        isv = True
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l > 0:
                    l -= 1
                else:
                    isv = False
        return l, isv
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ansl = len(s)+1
        ans = []
        q = Queue.Queue()
        dic = Set([s])
        q.put(s)
        while not q.empty():
            st = q.get()
            if ansl < len(s)-len(st):
                break
            l, isv = self.isvalid(st)
            if l == 0 and isv:
                ansl = len(s)-len(st)
                ans.append(st)
            elif ansl == len(s)+1:
                for i in range(len(st)):
                    if (l > 0 and st[i] == '(') or (l < 0 and st[i] == ')') or (l == 0 and st[i] in ['(', ')']):
                        newSt = st[:i]+st[i+1:]
                        if not (newSt in dic):
                            dic.add(newSt)
                            q.put(newSt)
        return ans