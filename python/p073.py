#Use the first row and first column to store the status of each row and column
#But pre-check if the row1 and col1 should be set zero
#scan all the elements except the first row and column, update to row1 col1
#according to row1, col1, update the elements
#based on the result of pre-check, update row1 col1
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix); 
        if m == 0:
            return []
        n = len(matrix[0])
        zerom = 0; zeron = 0
        for i in range(m):
            if matrix[i][0] == 0:
                zerom = 1
        for j in range(n):
            if matrix[0][j] == 0:
                zeron = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if zerom:
            for i in range(m):
                matrix[i][0] = 0
        if zeron:
            for i in range(n):
                matrix[0][i] = 0