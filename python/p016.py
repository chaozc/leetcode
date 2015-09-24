#Similar to P015 3Sum
#change 0 to target
#O(n2)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        i = 0; a = []; noa = []
        while i < n:
        	j = i
        	while j < n and nums[j] == nums[i]:
        		j += 1
        	a.append(nums[i])
        	noa.append(j-i)
        	i = j

        na = len(a)
        ans = 0
        m = -1
        for i in range(na):
        	if m == 0:
        		break
        	if noa[i] < 2:
        		l = i+1
        	else:
        		l = i
        	r = na-1;
        	while l <= r:
        		if r == l and noa[l] < 2:
        			break
        		if r == i and noa[l] < 3:
        			break

        		s = a[l]+a[i]+a[r]
        		if abs(s-target) < m or m == -1:
        			m = abs(s-target)
        			ans = s
        		if s == target:
        			break
        			l += 1
        			r -= 1
        		elif s > target:
        			r -= 1
        		else:
        			l += 1
        return ans
if __name__ == "__main__":
	a = Solution()
	print a.threeSumClosest([1, 1, -1, -1, 3], 3)