class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        per = [i for i in range(n)]
        tot = 1
        for i in range(n):
            tot *= (i+1)
        ans = [nums]
        for m in range(tot-1):
            for i in range(n-2, -1, -1):
                if per[i] < per[i+1]:
                    break
            for j in range(n-1, -1, -1):
                if per[j] > per[i]:
                    break
            k = per[i]; per[i] = per[j]; per[j] = k;
            p = i
            for i in range(p+1, n):
                j = n+p-i
                if i < j:
                    k = per[i]; per[i] = per[j]; per[j] = k;
                else:
                    break
            ans.append([nums[per[i]] for i in range(n)])
        return ans