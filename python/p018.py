#firstly count sum2
#for each sum2i, use binary search to find sum2j that sum2i+sum2j = target
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        a = []; dic = {}
        i = 0
        while i < n:
        	j = i
        	while j < n and nums[j] == nums[i]:
        		j += 1
        	a.append(nums[i])
        	dic[nums[i]] = j-i
        	i = j

        na = len(a)
        b = []
        for i in range(na):
        	if dic[a[i]] > 1:
        		k = i
        	else:
        		k = i+1
        	for j in range(k, na):
        		b.append([a[i]+a[j], a[i], a[j]])
        
        nb = len(b)
        b.sort()
        ans = []
        for i in range(nb):
        	l = i; r = nb-1
        	while l <= r:
        		mid = (l+r)/2
        		if b[mid][0] == target-b[i][0]:
        			break
        		elif b[mid][0] < target-b[i][0]:
        			l = mid+1
        		else:
        			r = mid-1
        	if b[mid][0] == target-b[i][0] and i <= mid:
        		i1 = mid;
        		while i1 >= i and b[i1][0] == b[mid][0]:
        			i1 -= 1
        		i1 += 1
        		i2 = mid

        		while i2 < nb and b[i2][0] == b[mid][0]:
        			i2 += 1

        		for j in range(i1, i2):

        			ele = [b[i][1], b[i][2], b[j][1], b[j][2]]
        			ele.sort()
        			d = {}
        			for it in ele:
        				if not d.has_key(it):
        					d[it] = 0
        				d[it] += 1
        			flag = True

        			for it in d.keys():
        				if d[it] > dic[it]:
        					flag = False
        					break

        			if flag:
        				ans.append(ele)
        ans.sort(key=lambda x:(x[0], x[1], x[2], x[3]))
        rt = []
        i = 0
        while i < len(ans):
        	rt.append(ans[i])
        	j = i
        	while (j < len(ans) and ans[j][0] == ans[i][0] and ans[j][1] == ans[i][1] and ans[j][2] == ans[i][2] and ans[j][3] == ans[i][3]):
        		j += 1
        	i = j
        return rt
if __name__ == "__main__":
	a = Solution()
	print a.fourSum([0, 0], 0)