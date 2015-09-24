#ms: a list of numbers whose ids are in the range of [i-k+1, i]
#ids: the corresponding ids for elements in ms
#l and r suggest the valid range for ms, that is for ms[i], where i is not in [l, r], ms[i] is not valid
#for l<=i<=j<=r, ms[i]>ms[j], insert a ms[i] each time, where i = r+1, if ms[i]>ms[i-1], i = i-1
#output ms[l] each time
#O(n)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
        	return []
       	ms = [nums[0]]
       	ids = [0]

       	l = 0
       	r = 0
       	length = len(nums)
       	if length == 1:
       		return ms
       	ans = []
       	if k == 1:
       		ans.append(ms[0])
       	for i in range(1, length):
       		j = r+1
       		while ((j > l) and (nums[i] > ms[j-1])):
       			j -= 1
       		if j == r+1:
       			ms.append(nums[i])
       			ids.append(i)
       		ms[j] = nums[i]
       		ids[j] = i
       		r = j
       		while ids[l] < i-k+1:
       			l += 1
       		if i >= k-1:
       			ans.append(ms[l])
       		#print ans, ids, ms, l, r
       	return ans

if __name__ == "__main__":
	a = Solution()
	print a.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)