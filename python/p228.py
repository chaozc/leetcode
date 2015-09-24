#Scan from left to right, check if num[i] = num[i-1]+1
#O(n)
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        if n == 0:
        	return []
        ans = []
        start = nums[0]
        end = nums[0]
        nums.append(nums[n-1]+2)
        for i in range(1, n+1):
        	if nums[i] == end+1:
        		end += 1
        	else:
    			st = str(start)
    			if start < end:
    				st += "->"+str(end)
    			ans.append(st)
    			start = nums[i]
    			end = nums[i]
    	return ans
if  __name__ == "__main__":
	a = Solution()
	print a.summaryRanges([0,1,2,4,5,7])