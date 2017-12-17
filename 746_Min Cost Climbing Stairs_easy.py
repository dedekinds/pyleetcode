
'''
746. Min Cost Climbing Stairs
2017.12.17
'''

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        temp=cost[::-1]
        dp=[0]*len(cost)
        dp[0]=temp[0]
        dp[1]=min(temp[0], temp[1])
        for x in range(1,len(cost)):
            dp[x]=temp[x]+min(dp[x-1], dp[x-2])
        return min(dp[-1],dp[-2])
        
        


        一开始这里下面想用贪心试一波，结果妥妥WA，然后才想到要用DP
        '''
         tempans_0=0
        tempans_1=0   
        length=len(cost)
        cost=cost+[0,0]
        #index 0
        t=0
        tempans_0=cost[0]
        while t<=length-1:
            if cost[t+1]<cost[t+2]:
                tempans_0+=cost[t+1]
                t+=1
            else:
                tempans_0+=cost[t+2]
                t+=2
        #index1
        t=1
        tempans_1=cost[1]
        while t<=length-1:
            if cost[t+1]<cost[t+2]:
                tempans_1+=cost[t+1]
                t+=1
            else:
                tempans_1+=cost[t+2]
                t+=2
        print(tempans_0,tempans_1)
        return min(tempans_0,tempans_1)
        
        '''
