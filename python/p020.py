class Solution:
    # @return a boolean
    def isValid(self, s):
        l = ['(', '{', '[']
        r = [')', '}', ']']
        pair = {')':'(', '}':'{', ']':'['}
        stack = []
        for ch in s:
            if ch in l:
                stack.append(ch)
            elif ch in r:
                if len(stack) == 0 or stack.pop() != pair[ch]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) > 0:
                    cc = stack.pop()
                else:
                    return False
                if not ((cc == '(' and c == ')') or (cc == '[' and c == ']') or (cc == '{' and c == '}')):
                    return False
        return stack == []