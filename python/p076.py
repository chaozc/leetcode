#scan from left to right
#keep a standard dictionary:dic and a count dictionary cdic
#keep a quene q: q = {c|c in t and c in s}, in order
#keep cdic < dic, if not, move the left bound to the next character in q
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tot = len(t)

        dic = {}
        for w in t:
        	if not dic.has_key(w):
        		dic[w] = 0
        	dic[w] += 1

        length = len(s)
        ans = ''

        for left in range(length):
        	if s[left] in t:
        		break
    	cdic = {}
    	q = []
    	l = 0
    	r = -1
    	cnt = 0
    	for i in range(left, length):
    		if s[i] in t:
    			if not cdic.has_key(s[i]):
    				cdic[s[i]] = 0
    			cdic[s[i]] += 1
    			q.append(i)
    			r += 1
    			if cdic[s[i]] <= dic[s[i]]:
    				cnt += 1
    			
    			while cdic[s[q[l]]] > dic[s[q[l]]]:
    				cdic[s[q[l]]] -= 1
    				l += 1
    				left = q[l]
    			if cnt == tot:
    				if q[r]-q[l]+1 < len(ans) or ans == '':
    					ans = s[q[l]:q[r]+1]
    			#print cdic, q, ans
        return ans

if __name__ == "__main__":
	a = Solution()
	print a.minWindow('A', 'AA')