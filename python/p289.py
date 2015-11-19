class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) > 0 and len(board[0]) > 0:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    cnt = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if dx != 0 or dy != 0:
                                x = i+dx; y = j+dy;
                                if (x > -1 and x < len(board)) and (y > -1 and y < len(board[0])) and board[x][y]%2 == 1:
                                    cnt += 1
                    if board[i][j] == 1:
                        if cnt >= 2 and cnt <= 3:
                            board[i][j] = 3
                    else:
                        if cnt == 3:
                            board[i][j] = 2
            for i in range(len(board)):
                for j in range(len(board[0])):
                    board[i][j] /= 2