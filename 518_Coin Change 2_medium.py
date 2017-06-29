'''518. Coin Change 2 
   2017.6.29

'''
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp=[[0]*(len(coins)+1) for x in range(amount+1)]
        #初始化
        for y in range(amount+1):
            dp[y][0]=0
        for x in range(len(coins)+1):
            dp[0][x]=1
        #dp[i][j]=dp[i][j-1]+dp[i-conins[j]][j]
        for i in range(amount):
            for j in range(len(coins)):
                tempi=i+1
                tempj=j+1
                if tempi>=coins[tempj-1]:
                    dp[tempi][tempj]=dp[tempi][tempj-1]+dp[tempi-coins[tempj-1]][tempj]
                else:
                    dp[tempi][tempj]=dp[tempi][tempj-1]                  
        return dp[-1][-1]


见博客