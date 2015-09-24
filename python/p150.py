#Stack
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        n = len(tokens)
        if n == 0:
        	return 0
        s = []; top = -1; size = 0;
        for i in range(n):
        	if tokens[i] == "+":
        		s[top-1] = s[top-1]+s[top]
        		top -= 1
        	elif tokens[i] == "-":
        		s[top-1] = s[top-1]-s[top]
        		top -= 1
        	elif tokens[i] == "*":
        		s[top-1] = s[top-1]*s[top]
        		top -= 1
        	elif tokens[i] == "/":
        		if s[top-1]*s[top] < 0 and s[top-1]%s[top] != 0:
        			s[top-1] = s[top-1]/s[top]+1
        		else:
        			s[top-1] = s[top-1]/s[top]
        		top -= 1
        	else:
        		if top+1 == size:
        			size += 1
        			s.append(0)
        		top += 1
        		s[top] = int(tokens[i])
        	#print tokens[i], s, s[top]
        return s[0]if __name__ == "__main__":
	a = Solution()
	print a.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"])