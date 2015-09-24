#two stack num & op
#first calculate all the * and /, update num & op
#scan from left to right: update: num[i] = num[i] op[i] num[i+1]

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        num = []; topn = -1; szn = 0;
        op = []; topo = -1; szo = 0;
        i = 0;
        while i < n:
        	if s[i] == ' ':
        		i += 1
        		continue
        	if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
        		if topo == szo-1:
        			szo += 1
        			op.append('.')
        		topo += 1
        		op[topo] = s[i]
        		i += 1
        	else:
        		j = i
        		while i < n and s[i] >= '0' and s[i] <= '9':
        			i += 1
        		number = int(s[j:i])
        		if topo > -1:
        			if op[topo] == '*':
        				num[topn] *= number
        				topo -= 1
        				number = -1
        			elif op[topo] == '/':
        				num[topn] /= number
        				topo -= 1
        				number = -1
        		if number >= 0:
        			if topn == szn-1:
        				szn += 1
        				num.append(0)
        			topn += 1
        			num[topn] = number
        	#print num, op, topn, topo
    	for i in range(topn):
    		#print i, op[i]
    		if op[i] == '+':
    			num[0] += num[i+1]
    		else:
    			num[0] -= num[i+1]
    	if topn > -1:
    		return num[0]
    	else:
    		return 0
if __name__ == "__main__":
	a = Solution()
	print a.calculate("3+2*2")

        