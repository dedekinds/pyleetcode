'''
121. Best Time to Buy and Sell Stock 
2017.11.28
'''
用temp_min记录并更新当前最小的数
然后从前到后遍历一次O(n)
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans=0
        if len(prices)<=1:
            return 0
        temp_min=prices[0]
        length=len(prices)
        t=0
        while t<length:
            if temp_min>prices[t]:
                temp_min=prices[t]
            else:
                ans=max(prices[t]-temp_min,ans)
            t+=1
        return ans
                

