#dfs: return all the subsets of num[st:en+1]
class Solution(object):
    def dfs(self, nums, st, en):
        ans = []
        for i in range(st, en+1):
            if i < en:
                re = self.dfs(nums, i+1, en)
            else:
                re = [[]]
            for it in re:
                ans.append([nums[i]]+it)
        ans.append([])
        return ans
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.dfs(nums, 0, len(nums)-1)
        