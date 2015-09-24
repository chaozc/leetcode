class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        ns = [(nums[i], i) for i in range(n)]
        ns.sort()
        for i in range(1, n):
            if ns[i][0] == ns[i-1][0] and abs(ns[i][1]-ns[i-1][1]) <= k:
                return True
        return False