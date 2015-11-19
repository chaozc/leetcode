class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []
        lower -= 1
        nums.append(upper+1)
        for num in nums:
            if num > lower+1:
                ans.append(str(lower+1))
                if num-1 > lower+1:
                    ans[-1] += '->'+str(num-1)
            lower = num
        return ans