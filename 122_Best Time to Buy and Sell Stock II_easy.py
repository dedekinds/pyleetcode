'''122. Best Time to Buy and Sell Stock II 
   2017.8.3
'''
把它画成一个坐标图的话，实际上即使找各个波峰和波谷的差，但是
为什么这样的贪心算法能够达到最优解呢？
看着自己的博客
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