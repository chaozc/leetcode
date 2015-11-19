#http://bangbingsyb.blogspot.com/2014/11/leetcode-longest-consecutive-sequence.html
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for (i, n) in enumerate(nums):
            dic[n] = i
        ans = 1;
        for i in range(len(nums)):
            l = 0; j = nums[i];
            while dic.pop(j, None) != None:
                l += 1
                j += 1
            j = nums[i]-1
            while dic.pop(j, None) != None:
                l += 1
                j -= 1
            ans = max(l, ans)
        return ans