#http://stackoverflow.com/questions/251781/how-to-find-the-kth-largest-element-in-an-unsorted-array-of-length-n-in-on
#quick selection
class Solution(object):
    def quickselect(self, nums, k):
        p = nums[0]
        big = []; small = []
        for it in nums[1:]:
            
            if it >= p:
                big.append(it)
            else:
                small.append(it)
        if k-1 == len(big):
            return nums[0]
        if k <= len(big):
            return self.quickselect(big, k)
        else:
            return self.quickselect(small, k-len(big)-1)
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickselect(nums, k)
        """
        ans = nums[:k]
        ans.sort()
        for i in range(k, len(nums)):
            if nums[i] > ans[0]:
                ans[0] = nums[i]
            for j in range(k-1):
                if ans[j] > ans[j+1]:
                    w = ans[j]; ans[j] = ans[j+1]; ans[j+1] = w;
                else:
                    break
        return ans[0]
        """