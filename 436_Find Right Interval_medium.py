'''
436. Find Right Interval 
2017.10.12
'''
对首位排序后用二分法搜索
import bisect
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        #temp=sorted(intervals,key=lambda x:x[0])  囧，本来直接intervals.sort()就已经是按第一个元排列了
        temp=sorted([x.start,i] for i,x in enumerate(intervals))
        #print(temp)
        check=[]
        ans=[]
        length=len(intervals)-1
        for x in temp:
            check.append(x[0])
        for x in intervals:
            x_insert_point = bisect.bisect_right(check,x.end)
            
            #print(x_insert_point,x,temp[-1][0]!=x[1])

            if x_insert_point>length and temp[-1][0]!=x.end:
                ans.append(-1)
            else:
                if temp[x_insert_point-1][0]==x.end:#这个判断上由于bisect_right导致的，目标数存在的话会返回其右边，所以要判断是不是目标数
                    ans.append(temp[x_insert_point-1][1])
                else:
                    ans.append(temp[x_insert_point][1])
        return ans
