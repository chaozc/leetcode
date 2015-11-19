class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        i = 0; j = len(s)-1;
        while i < j:
            while i < j and (not((s[i] <= 'z' and s[i] >= 'a')or(s[i] <= '9' and s[i] >= '0')or(s[i] <= 'Z' and s[i] >= 'A'))) :
                i += 1
            while i < j and (not((s[j] <= 'z' and s[j] >= 'a')or(s[j] <= '9' and s[j] >= '0')or(s[j] <= 'Z' and s[j] >= 'A'))) :
                j -= 1
            print i, j
            if i < j:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True

a = Solution()
print a.isPalindrome('ab@a')