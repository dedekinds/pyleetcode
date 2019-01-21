class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(word)
        
        def findpath(i,j,cnt):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):return False
            #print(cnt,'i=',i,'j=',j,board[i][j] == word[cnt],'word=',board[i][j])
            if board[i][j] == word[cnt]:
                if cnt == n-1:return True
                tmp = board[i][j]
                board[i][j] = '#'
                res = findpath(i,j+1,cnt+1) or findpath(i,j-1,cnt+1) or findpath(i+1,j,cnt+1) or findpath(i-1,j,cnt+1)
                if not res:
                    board[i][j] = tmp
                return res
            else:
                return False

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = findpath(i,j,0)
                if res:
                    return True
        return False
        
        