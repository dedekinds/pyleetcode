'''322. Coin Change 
   2017.6.30

'''
见博客

class Solution(object):
    def coinChange(self, coins, amount):
        dp=[233333333]*(amount+1)
        dp[0]=0
        for c in coins:
            for i in range(c,len(dp)):
                dp[i]=min(dp[i],dp[i-c]+1)
        if dp[-1]==233333333:
            return -1
        return dp[-1]

________TLE_____________
class Solution(object):
    def coinChange(self, coins, amount):
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