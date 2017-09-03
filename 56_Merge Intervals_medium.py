'''56. Merge Intervals 
   2017.9.3
'''
刚做了452. Minimum Number of Arrows to Burst Balloons 思路也很明确
画个图，按start排序后，逐步更新start和end
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return []
        intervals.sort(key=lambda x:x.start)
        
        start=intervals[0].start
        end=intervals[0].end
        ans=[]
        
        for temp in intervals:
            if temp.start<=end and temp.end>=end:
                end=temp.end
            elif temp.start>end:
                ans.append(Interval(start,end))
                start=temp.start
                end=temp.end
        ans.append(Interval(start,end))
        return ans