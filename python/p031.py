#http://fisherlei.blogspot.com/2012/12/leetcode-next-permutation.html
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                break
        if n > 1:
            if nums[i] >= nums[i+1]:
                nums.sort()
            else:
                for j in range(n-1, -1, -1):
                    if nums[j] > nums[i]:
                        break
                k = nums[i]; nums[i] = nums[j]; nums[j] = k;
                for p in range(i+1, n):
                    j = n+i-p
                    if p < j:
                        k = nums[p]; nums[p] = nums[j]; nums[j] = k;