class Solution(object):
        
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0] * len(days)
        def findlast(i,day):
            for j in range(i-1,-1,-1):
                if days[j] + day <= days[i]:
                    return dp[j]
            return 0
        for i in range(len(days)):
            dp[i] = min(costs[0]+findlast(i,1),costs[1]+findlast(i,7),costs[2]+findlast(i,30))
        return dp[-1]
                
        
        