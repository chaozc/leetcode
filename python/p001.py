class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        snums = [(i, nums[i]) for i in range(len(nums))]
        snums.sort(key=lambda x:x[1])
        i = 0; j = len(nums)-1
        while i < j:
            if snums[i][1]+snums[j][1] == target:
                return [min(snums[i][0], snums[j][0])+1, max((snums[i][0], snums[j][0]))+1]
            elif snums[i][1]+snums[j][1] < target:
                i += 1
            else:
                j -= 1