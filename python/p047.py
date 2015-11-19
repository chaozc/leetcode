class Solution(object):
    def dfs(self, nums, tmp, boo, n, left):
        if left == 0:
            tans = [it for it in tmp]
            self.ans.append(tans)
            return
        for i in range(n):
            if boo[i]:
                if i > 0 and nums[i] == nums[i-1] and (not boo[i-1]):
                    continue
                boo[i] = False
                tmp[n-left] = nums[i]
                self.dfs(nums, tmp, boo, n, left-1)
                boo[i] = True
                
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        self.ans = []
        boo = [True for i in range(n)]
        tmp = [0 for i in range(n)]
        self.dfs(nums, tmp, boo, n, n)
        return self.ans