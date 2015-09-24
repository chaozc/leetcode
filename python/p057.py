# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n == 0:
        	return [newInterval]
        ans = []
        for i in range(n):
        	if intervals[i].start >=  newInterval.start:
        		break
        if intervals[i].start < newInterval.start:
        	intervals.append(newInterval)
        else:
        	intervals.append(0)
        	for j in range(n, i, -1):
        		intervals[j] = intervals[j-1]
        	intervals[i] = newInterval

        m = -1
        for i in range(n+1):
        	#print i, intervals[i].start, intervals[i].end
        	#print m
        	if m == -1 or (ans[m].end < intervals[i].start):
        		m += 1
        		ans.append(intervals[i])
        	
        	else:
        		ans[m].end = max(ans[m].end, intervals[i].end)
        		
        return ans
        """
        print ans
        if intervals[i].end < newInterval.start:
        	ans.append(newInterval)
        else:
        	i -= 1
        	if :
        		tmp = newInterval
        		newInterval = intervals[0]
        		intervals[0] = tmp
        		if len(ans) == 1:
        			ans = []
        	else:
        		ans = ans[:-1]
        	print ans
        	if (intervals[i].end >= newInterval.start):
        		intervals[i].end = max(intervals[i].end, newInterval.end)
        	else:
        		ans.append(intervals[i])
        		intervals[i] = newInterval
        		print ans

        	j = i+1
        	for j in range(i+1, n):
        		if intervals[j].start <= intervals[i].end:
        			intervals[i].end = max(intervals[i].end, intervals[j].end)
        		else:
        			break
        	ans.append(intervals[i])
        	if j < n and intervals[j].start > intervals[i].end:
        		for k in range(j, n):
        			ans.append(intervals[k])
        """
        return ans

if __name__ == "__main__":
	a = Solution()
	intv = [Interval(1,3), Interval(6,9)]
	intv = [Interval(1,2), Interval(3,5),Interval(6,7), Interval(8,10),Interval(12,16)]
	#intv = [Interval(1,5)]
	newInterval = Interval(4,9)
	ans = a.insert(intv, newInterval)
	for it in ans:
		print it.start, it.end