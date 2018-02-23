'''
539. Minimum Time Difference
2018.2.23
'''
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        temp=sorted( map(int,p.split(':')) for p in timePoints )
        temp+=[  [temp[0][0]+24,temp[0][1]] ]
        #print(temp)
        #[[0, 0], [23, 59], [24, 0]]
        return min( (temp[x+1][0]-temp[x][0])*60+ temp[x+1][1]-temp[x][1] for x in range(len(temp)-1) )
    

        