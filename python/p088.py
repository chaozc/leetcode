class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        smallerthan = [0 for i in range(m)]
        i = 0
        for j in range(n):
            while i < m and nums1[i] < nums2[j]:
                smallerthan[i] = j
                i += 1
        while i < m:
            smallerthan[i] = n
            i += 1
        for i in range(m-1, -1, -1):
            nums1[i+smallerthan[i]] = nums1[i]
        i = 0;
        j = 0;
        for k in range(m+n):
            if m > i and k == (i+smallerthan[i]):
                i = i+1
            else:
                nums1[k] = nums2[j]
                j = j+1