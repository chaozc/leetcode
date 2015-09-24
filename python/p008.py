class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ans = 0
        if len(str) == 0:
        	return 0

        while len(str) > 1 and str[0] == ' ':
        	str = str[1:]
        #print str
        if str == ' ':
        	return 0

        neg = 0
        if str[0] == '-' or str[0] == '+':
        	if str[0] == '-':
        		neg = 1
        	str = str[1:]
        	
        str += '.'
        for i in range(len(str)):
        	if str[i] > '9' or str[i] < '0':
        		break
        str = str[:i]
        while len(str) > 1 and str[0] == '0':
        	str = str[1:]
        str = str[::-1]
        base = 1
        ans = 0
        for i in range(len(str)):
        	ans += base*int(str[i])
        	base *= 10
        if ans >= 2147483648:
        	if neg == 0:
        		ans = 2147483647
        	elif ans > 2147483648:
        		ans = 2147483648
        if neg:
        	ans = -ans
        return ans
if __name__ == "__main__":
	a = Solution()
	print a.myAtoi("2147483648")