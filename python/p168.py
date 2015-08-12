class Solution:
    # @return a string
    def convertToTitle(self, num):
        ans = ''
        while num > 0:
        	num -= 1
        	ans = chr((num)%26+ord('A'))+ans
        	num /= 26
        return ans