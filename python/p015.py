#Sort
#for i, let i < l < r, l:i->n, r:n->i
#find a[i]+a[l]+a[r]=0
#O(n2)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
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
        ans = []
        for i in range(na):
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
        		if s == 0:
        			ans.append([a[i], a[l], a[r]])
        			l += 1
        			r -= 1
        		elif s > 0:
        			r -= 1
        		else:
        			l += 1
        return ans
if __name__ == "__main__":
	a = Solution()
	print a.threeSum([-1, 0, 1, 2, -1, -4])