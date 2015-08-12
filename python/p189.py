class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        tmp = []
        for i in range(n):
            tmp.append(nums[i])
        for i in range(n):
            nums[(i+k)%n] = tmp[i]