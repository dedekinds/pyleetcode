
累计和，遇到<0累计和的时候，舍弃，重新从0开始算

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 0:
            return 0
        if len(array) == 1:
            return array[0]
        opt = array[0]
        acc_sum = array[0]
        for i in range(1,len(array)):
            acc_sum += array[i]
            if acc_sum > opt:
                opt = acc_sum
            if acc_sum < 0:
                acc_sum = 0
        return opt
        