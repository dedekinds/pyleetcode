'''
780. Reaching Points
2018.2.11
'''
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        #倒过来看像是辗转相除法的说。。试一试
        
        '''
        首先注意到两个坐标位置都只能递减，不断用辗转相除来递减，如果递减到小于初始值的话就False，否则的话总有一个时刻是至少有一个坐标位置的值是相同的（否     则一定能通过下一步的辗转相除，使得某个坐标位置小于初始值），此时再看，另一个坐标位置是否能通过不断减已经相等的那个坐标位置的值达到初始值即可

        '''
        while(tx>=sx and ty>=sy):#两个坐标位置都只能递减
            if tx>=ty:
                if ty==sy:return (tx-sx)%ty==0
                tx=tx%ty
            else:
                if tx==sx:return (ty-sy)%tx==0
                ty=ty%tx
        return False