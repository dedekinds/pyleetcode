'''122. Best Time to Buy and Sell Stock II 
   2017.8.3
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans=0
        if len(prices)<=1:
            return 0
        for x in range(1,len(prices)):
            if prices[x]-prices[x-1]>=0:
                ans+=prices[x]-prices[x-1]
        return ans