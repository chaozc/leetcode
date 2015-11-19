class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort()
        ans = 0
        for i in range(len(nums)-2):
            for j in range(len(nums)-2, i, -1):
                if nums[i]+nums[j]+nums[j+1] < target:
                    break
            if nums[i]+nums[j]+nums[j+1] >= target:
                break
            k = j+1
            jj = j
            for j in range(jj, i, -1):
                ans += k-j
                k += 1
                while k < len(nums) and nums[i]+nums[j]+nums[k] < target:
                    k += 1
                    ans += 1
                k -= 1
        return ans
                   