'''554. Brick Wall 
   2017.6.10
   未通过超时
'''

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        ans=99999999
        minres=0
        for x  in range(1,sum(wall[0])):
            #print('wall=',wall)
            #print('ans=',ans)
            for y in range(len(wall)):
                if wall[y][0]==1:
                    wall[y]=wall[y][1:]
                else:
                    minres+=1
                    wall[y][0]-=1
            if minres<ans:
                ans=minres
            minres=0
        return ans
                    
            

      
wall=[[100000000],[100000000],[100000000]]
temp=Solution()
print(temp.leastBricks(wall))
#print(binsearch(nums,target))


#wall=[[100000000],[100000000],[100000000]]

