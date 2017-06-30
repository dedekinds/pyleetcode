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


——————————————
BFS：https://discuss.leetcode.com/topic/32589/fast-python-bfs-solution
DFS：https://discuss.leetcode.com/topic/36306/python-11-line-280ms-dfs-with-early-termination-99-up



import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp = [(amount+1) for i in xrange(amount+1)]
        # dp[0] = 0
        # for am in xrange(amount+1):
        #     for j, coin in enumerate(coins):
        #         if coin <= am:
        #             dp[am] = min(1+dp[am-coin], dp[am])
        # return dp[amount] if dp[amount] != amount+1 else -1
########################################
        if amount == 0:
            return 0
        if not coins:
            return -1
        coins.sort(reverse = True)
        maxc = amount//coins[-1] + (amount%coins[-1]==0) # 1+maximum possible
        self.ans = maxc

        def dfs(i, ncoin, target):
            while i < len(coins) and coins[i] > target:
                i += 1
            if i == len(coins):
                return
            minc = (target//coins[i]) + (target%coins[i] != 0) # min possible

            if minc + ncoin >= self.ans: # no need to go further
                return
            if target%coins[i] == 0: # can use this only
                self.ans = minc + ncoin
            else:
                dfs(i, ncoin+1, target-coins[i])
                dfs(i+1, ncoin, target)
            return

        dfs(0, 0, amount)
        return self.ans if self.ans != maxc else -1
