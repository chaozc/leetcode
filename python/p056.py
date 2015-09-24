# Sort and merge one by one
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
    	self.start = s
    	self.end = e

class Solution(object):
    def sort(self, l, r, intervals):
		i = l
		j = r
		mid = intervals[(l+r)/2]
		#print '***', mid, intervals[mid].start
		while (i <= j):
			while (intervals[i].start < mid.start):
				i += 1
			while (intervals[j].start > mid.start):
				j -= 1
			#print i, j
			if i <= j:
				tmp = intervals[i]
				intervals[i] = intervals[j]
				intervals[j] = tmp
				i += 1
				j -= 1
		"""
		print '------', l, r, mid, i, j
		for it in intervals:
			print it.start, it.end
		print '------'
		"""
		if l < j:
			intervals = self.sort(l, j, intervals)
		if i < r:
			intervals = self.sort(i, r, intervals)
		return intervals
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n == 0:
        	return []
        intervals = self.sort(0, n-1, intervals)
        """
        for it in intervals:
			print it.start, it.end
		"""
        ans = [intervals[0]]
        m = 0
        for i in range(1, n):
        	if intervals[i].start > ans[m].end:
        		ans.append(intervals[i])
        		m += 1
        	else:
        		ans[m].end = max(ans[m].end, intervals[i].end)
        return ans
if __name__ == "__main__":
	a = Solution()
	intv = [Interval(1,4),Interval(0,4)]
	#intv = [Interval(2,6),Interval(8,10),Interval(15,18),Interval(1,3)]
	#intv = [Interval(4,5),Interval(3,5),Interval(5,6),Interval(0,0),Interval(2,2),Interval(4,5),Interval(2,2)]
	#intv = [Interval(1,2), Interval(0,1),Interval(0,1)]
	ans =  a.merge(intv)
	print
	for it in ans:
		print it.start, it.end