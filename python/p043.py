class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        while len(num1) > 0 and num1[0] == '0':
            num1 = num1[1:]
        while len(num2) > 0 and num2[0] == '0':
            num2 = num2[1:]
        if num1 == "" or num2 == "":
            return "0"
        n1 = len(num1); n2 = len(num2);
        ans = [0 for i in range(n1+n2)]
        for i in range(n1):
            for j in range(n2):
                ans[i+j] += int(num1[n1-1-i])*int(num2[n2-1-j])
        i = 0; c = 0;
        for i in range(n1+n2):
            ans[i] += c
            c = ans[i]/10
            ans[i] %= 10
            i += 1
        st = ""
        i = n1+n2-1
        while ans[i] == 0:
            i -= 1
        while i >= 0:
            st += str(ans[i])
            i -= 1
        return st