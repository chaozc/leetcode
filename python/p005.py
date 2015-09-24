#Manachar Algorithm
#http://www.felix021.com/blog/read.php?2040
#O(n)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
        	return ''
        ps = "#"
        for ch in s:
        	ps += ch+"#"

        m_id = 0
        m = 0
        n = len(ps)
        f = [0]*n
        f[0] = 1
        ans = 1
        ansm = 0
        for i in range(1, n):
        	f[i] = 1
        	j = 2*m_id-i
        	if i < m:
        		if f[j] < m-i+1:
        			f[i] = f[j]
        		else:
        			f[i] = m-i+1
        	while i-f[i]+1 >= 0 and i+f[i]-1 < n and ps[i+f[i]-1] == ps[i-f[i]+1]:
        		f[i] += 1
        	f[i] -= 1
        	if i+f[i]-1 > m:
        		m = i+f[i]-1
        		m_id = i
        	if ans <= f[i]-1:
        		ans = f[i]-1
        		ansm = i
        anss = ""
        for i in range(ansm-ans, ansm+ans+1):
        	if i%2 == 1:
        		anss += ps[i]
        	#print i, ps[i], f[i]-1
        #print ps, ansm, ans
        return anss
if __name__ == "__main__":
	a = Solution()
	print a.longestPalindrome('a')