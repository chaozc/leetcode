class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        st = [s[j-10+1:j+1] for j in range(9, len(s))]
        st.sort()
        i = 0; ans = []
        #print st
        while i < len(st):
            j = i;
            while j < len(st) and st[j] == st[i]:
                j += 1
            if j-i > 1:
                ans.append(st[i])
            i = j
        return ans