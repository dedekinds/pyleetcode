# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x.start)
        start = intervals[0].start
        end = intervals[0].end
        ans = []
        for temp in intervals:
            if temp.start <= end and end <= temp.end:
                end = temp.end
            elif temp.start > end:
                ans.append(Interval(start,end))
                start = temp.start
                end = temp.end
        ans.append(Interval(start,end))
        return ans
套入56.merge interval 问题即可