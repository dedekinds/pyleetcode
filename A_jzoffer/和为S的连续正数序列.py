

双指针+等差数列求和，不断逼近tsum，知道small>=(tsum+1)/2

# -*- coding:utf-8 -*-
class Solution:
    def get_sum(self,small,big):
        return int((small+big)*(big-small+1)/2)
    def FindContinuousSequence(self, tsum):
        # write code here282
        if tsum <= 2:return []
        res = []
        small = 1
        big = 2
        while small <= (tsum+1)/2:
            if self.get_sum(small,big) < tsum:
                big += 1
                continue
            if self.get_sum(small,big) > tsum:
                small += 1
                continue
            if self.get_sum(small,big) == tsum:
                res.append(range(small,big+1))
                small += 1
        return res
            
            