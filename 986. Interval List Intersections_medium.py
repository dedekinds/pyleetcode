# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
用了56. Merge Intervals的办法，再分类讨论
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        intervals = A + B
        if len(intervals) == 0:return []
        res = []
        intervals.sort(key = lambda x:x.start)
        start = intervals[0].start
        end = intervals[0].end
        #print(start,end)
        for tmp in intervals:
            if tmp.start < end and tmp.end <= end:
                res.append(Interval(tmp.start,tmp.end))
            if tmp.start < end and tmp.end > end:
                res.append(Interval(tmp.start,end))
                start = tmp.start
                end = tmp.end
            if tmp.start == end:
                res.append(Interval(end,end))
                start = tmp.start
                end = tmp.end
            if tmp.start > end:
                start = tmp.start
                end = tmp.end
                
                    
                    
        res.pop(0)
        return res
 