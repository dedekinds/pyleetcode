'''
789. Escape The Ghosts
2018.2.25
'''
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        若存在距离相等，那么鬼只要和玩家一样的走法，玩家一定不能胜利
        若距离比玩家到目标点的距离短的话，鬼总可以守在目标旁边或者走在目标和玩家之间，此时玩家一定不能胜利
        若距离都比玩家的长，玩家只要走最优的那条路线即可
        """
        
        myself=abs(target[0])+abs(target[1])
        for x in ghosts:
            if myself>=abs(target[0]-x[0])+abs(target[1]-x[1]):
                return False
        return True
                