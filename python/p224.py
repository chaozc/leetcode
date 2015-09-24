#two stack:num, op
#scan: if s[i] is op, push to op, if ')', check the previous '(' and pop
#else if op[topo] in ['+', '-'], calculate and update num[top] and pop op[topo]

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
    	num = []; szn = 0; topn = -1;
    	op = []; szo = 0; topo = -1;
    	i = 0
    	while i < n:
    		if s[i] == ' ':
    			i += 1
    			continue
    		#check if op
    		if s[i] == '(' or s[i] == ')' or s[i] == '+' or s[i] == '-':
    			if topo+1 == szo:
    				szo += 1
    				op.append('.')
    			topo += 1
    			op[topo] = s[i]
    			i += 1
    			if op[topo] == ')':
					topo -= 2
					if op[topo] == '+':
						num[topn-1] += num[topn]
						topn -= 1
						topo -= 1
					elif op[topo] == '-':
						num[topn-1] -= num[topn]
						topn -= 1
						topo -= 1
    		else: #if num
    			j = i
    			while i < n and s[i] <= '9' and s[i] >= '0':
    				i += 1
    			number = int(s[j:i])
    			#if op[top] = '('
    			if topo == -1 or op[topo] == '(':
    				if topn+1 == szn:
    					szn += 1
    					num.append(number)
    				topn += 1
    				num[topn] = number
    			else:
    				if op[topo] == '+':
    					num[topn] += number
    				else:
    					num[topn] -= number
    				topo -= 1
    	if topn < 0:
    		return 0
    	else:
    		return num[0]if __name__ == "__main__":
	a = Solution()
	print a.calculate("(3-(2-(5-(9-(4)))))")