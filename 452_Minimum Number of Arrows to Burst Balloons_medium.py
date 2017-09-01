'''452. Minimum Number of Arrows to Burst Balloons 
   2017.9.1
'''
下面的操作也是未加证明妈的：
首先将这些气球进行排序，然后我们可以发现，多个气球如果能一下子串起来，
那么可穿区间必是以某个气球的start和某个end组成的

设置箭为0x7FFFFFFF，我们从头到尾开始遍历，由于是从头开始遍历，所以start必是目前最小的，如果
当前箭比新的start小，说明穿不来，ans+=1，否则则说明有重合，更新箭的位置

（实际上上面的过程画个图比较容易

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)==0:
            return 0
        test=sorted(points)#直接排序的话是按照第一个排
        ans=1
        pointer=0x7FFFFFFF
        for a,b in test:
            if a>pointer:
                ans+=1
                pointer=0x7FFFFFFF
            pointer=min(pointer,b)
        return ans
