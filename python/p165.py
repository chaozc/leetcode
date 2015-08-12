class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def put(self, s, k):
        while len(s) < k:
            s = '0'+s
        return s
    def putl(self, l, k):
        while len(l) < k:
            l.append('0')
        return l
    def compareVersion(self, version1, version2):
        l1 = version1.split('.')
        l2 = version2.split('.')
        l = max(len(l1), len(l2))
        l1 = self.putl(l1, l)
        l2 = self.putl(l2, l)
        for i in range(l):
            ll = max(len(l1[i]), len(l2[i]))
            l1[i] = self.put(l1[i], ll)
            l2[i] = self.put(l2[i], ll)
            if l1[i] > l2[i]:
                return 1
            if l1[i] < l2[i]:
                return -1
        return 0