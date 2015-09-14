from sys import argv;
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
       	if x < 0:
		return False;
	if x == 0:
		return True;
	v = [];
	while x > 0:
		v.append(x%10);
		x = x/10;
	l = len(v);
	for i in range(l):
		if v[i] != v[l-i-1]:
			return False;
	return True;

if __name__ == "__main__":
	x = int(argv[1]);
	sol = Solution();
	print sol.isPalindrome(x);
