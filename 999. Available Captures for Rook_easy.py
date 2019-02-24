class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        for m in range(8):
            for n in range(8):
                if board[m][n] == 'R':
                    location = [m,n]
                    break
        res = 0
        m = location[0]
        n = location[1]
        for i in range(location[0]+1,8):
            if board[i][n] == 'B':
                break
            if board[i][n] == 'p':
                res += 1
                break
        for i in range(location[0],-1,-1):
            if board[i][n] == 'B':
                break
            if board[i][n] == 'p':
                res += 1
                break
        for j in range(location[1]+1,8):
            if board[m][j] == 'B':
                break
            if board[m][j] == 'p':
                res += 1
                break
        for j in range(location[1],-1,-1):
            if board[m][j] == 'B':
                break
            if board[m][j] == 'p':
                res += 1
                break
        return res