class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == None:
            return False
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if target > matrix[-1][-1]:
            return False
            
        l = 0; r = n-1;
        while l < r:
            mid = (l+r)/2
            if matrix[mid][-1] < target:
                l = mid+1
            else:
                r = mid
        row = l
        l = 0; r = m-1;
        while l < r:
            mid = (l+r)/2
            if matrix[row][mid] < target:
                l = mid+1
            else:
                r = mid
        if matrix[row][l] == target:
            return True
        else:
            return False