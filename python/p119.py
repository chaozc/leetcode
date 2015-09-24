class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [0 for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            ans[i] = 1; ans[0] = 1
            for j in range(i-1, 0, -1):
                ans[j] += ans[j-1]
        return ans
if __name__ == "__main__":
    a = Solution()
    print a.getRow(4)