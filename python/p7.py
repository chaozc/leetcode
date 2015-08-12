class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
    	st = str(x)
    	ans = ''
    	if st[0] == '-':
    		st = st[1:]
    		ans = '-'
    	ans += st[::-1]
    	if abs(int(ans)) > pow(2, 31):
    		ans = '0'
    	return int(ans)