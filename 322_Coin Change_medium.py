'''322. Coin Change 
   2017.6.30

'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        temp=233333333333333333333
        dp=[[0]*(len(coins)+1) for x in range(amount+1)]
        for x in range(amount+1):
            dp[x][0]=temp
        for i in range(amount):
            for j in range(len(coins)):
                tempi=i+1
                tempj=j+1
                if tempi>=coins[tempj-1]:
                    dp[tempi][tempj]=min(dp[tempi][tempj-1],1+dp[tempi-coins[tempj-1]][tempj])
                else:
                    dp[tempi][tempj]=dp[tempi][tempj-1]
        if dp[-1][-1]==temp:
            return -1
        return dp[-1][-1]