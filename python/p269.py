import Queue
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        edges = [[False for i in range(26)] for j in range(26)]
        d = [0 for i in range(26)]
        show = [False for i in range(26)]
        for w in words:
            for c in w:
                show[ord(c)-ord('a')] = True
                
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                for k in range(min(len(words[i]), len(words[j]))):
                    if words[i][k] != words[j][k]:
                        if not edges[ord(words[i][k])-ord('a')][ord(words[j][k])-ord('a')]:
                            edges[ord(words[i][k])-ord('a')][ord(words[j][k])-ord('a')] = True
                            d[ord(words[j][k])-ord('a')] += 1
                        break

        ans = ''
        q = Queue.Queue()
        for i in range(26):
            if d[i] == 0 and show[i]:
                q.put(i)
                
        while not q.empty():
            i = q.get()
            ans += chr(i+ord('a'))
            for j in range(26):
                if edges[i][j]:
                    d[j] -= 1
                    if d[j] == 0:
                        q.put(j)

        for i in range(26):
            if d[i] > 0:
                return ''
        return ans