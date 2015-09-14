class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        pos = {}
        if s == '':
        	ans = 0
        else:
        	ans = 1
        st = 0
        for i in range(len(s)):
        	if pos.has_key(s[i]):
        		if pos[s[i]] >= st:
        			ans = max(ans, i-st)
        			st = pos[s[i]]+1
        	pos[s[i]] = i
        ans = max(ans, len(s)-st)
        return ans