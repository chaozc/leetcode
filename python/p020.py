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
        