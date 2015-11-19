class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        ans = ''
        for st in strs:
            for c in st:
                if c == ',' or c == '|':
                    ans += '|'
                ans += c
            ans += ','
        return ans
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ans = []
        st = ''
        i = 0
        while i < len(s):
            if s[i] == '|':
                st += s[i+1]
                i += 2
            elif s[i] == ',':
                ans.append(st)
                i += 1
                st = ''
            else:
                st += s[i]
                i += 1
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))