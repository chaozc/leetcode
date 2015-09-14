#i: 1->max
#compare strs[k][i], check if they are the same
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        ans = ''
       	i = -1
        while True:
        	i += 1
        	ch = ''
        	for j in range(length):
        		if len(strs[j]) == i:
        			ch = ''
        			break
        		if (ch != ''):
        			if (ch != strs[j][i]):
        				ch = ''
        				break
        		else:
        			ch = strs[j][i]
        	if ch == '':
        		break
        	else:
        		ans += ch
        return ans
if __name__ == "__main__":
	a = Solution()
	print a.longestCommonPrefix(['dadddda', 'daddda', 'dadd'])