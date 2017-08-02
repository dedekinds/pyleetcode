'''419. Battleships in a Board 
   2017.8.2
'''

O(n2)暴力，对于一个字符，如果它左边或者上边是X那么不用理，否则+1
就这么暴力。。
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board)==0:
            return 0
        ans=0
        for x in range(len(board):
            for y in range(len(board[0])):
                if board[x][y]=='X':
                    if board[x-1][y]=='X' and x>0:
                        continue
                    if board[x][y-1]=='X' and y>0:
                        continue
                    else:
                        ans+=1
        return ans
