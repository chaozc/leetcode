class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
    	length = len(num)
    	lnum = [(num[i], i+1) for i in range(length)]
        lnum.sort(key=lambda x:x[0])
        for i in range(length):
        	t = target-lnum[i][0]
        	l = 0
        	r = length-1
        	while l < r:
        		mid = (l+r)/2
        		if lnum[mid][0] == t and mid != i:
        			l = mid
        			break
        		elif lnum[mid][0] > t:
        			r = mid
        		else:
        			l = mid+1
        	if lnum[l][0] == t:
        		return(min(lnum[i][1], lnum[l][1]), max(lnum[i][1], lnum[l][1]))
