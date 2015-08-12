class Solution:
    # @return a string
    def convert(self, s, nRows):
        ans = ''
        patternLen = 2*nRows-2
        if patternLen == 0:
        	patternLen = 1
        dRow = patternLen
        for i in range(nRows):
        	j = i
        	while j < len(s):
        		ans += s[j]
        		if dRow%patternLen > 0 and j+dRow < len(s):
        			ans += s[j+dRow]
        		j += patternLen
        	dRow -= 2
        return ans