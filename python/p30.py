#l: the length for each word
#idea: check all the substrs whose length is l, compare with the count dictionary
#scan: start from the first l character, move l towards right, if not match the count dictionary, move the left bound, with length l
#O([l*(n/l)]*l)扫描的复杂度为O(n), 匹配复杂度l,整体O(nl)
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        length = len(s)
        if n == 0 or length == 0:
        	return []

        dic = {}
        for w in words:
        	if not dic.has_key(w):
        		dic[w] = 0
        	dic[w] += 1
        l = len(w)
        ans = []

        for i in range(l):
			cdic = {}
			left = i
			cnt = 0
			for j in range(left, length, l):
				if (left+l*n > length):
					break
				w = s[j:j+l]
				if not dic.has_key(w):
					left = j+l
					cnt = 0
					cdic = {}
					continue
				else:
					if not cdic.has_key(w):
						cdic[w] = 0
					if cdic[w] < dic[w]:
						cdic[w] += 1
						cnt += 1
					else:
						while cdic[w] == dic[w]:
							ww = s[left:left+l]
							cnt -= 1
							cdic[ww] -= 1
							left += l
						cdic[w] += 1
						cnt += 1
					if cnt == n:
						ans.append(left)
						w = s[left:left+l]
						cdic[w] -= 1
						cnt -= 1
						left += l
        return ans
        


if __name__ == "__main__":
	a = Solution()
	print a.findSubstring('barfoothefoobarman', ['foo', 'bar'])