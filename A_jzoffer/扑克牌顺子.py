统计几个量，在过程中，如果有重复的数字的话直接返回false
  
0的个数
非0的个数
MAX
MIN

(MAX - MIN +1) - 非零个数 → 需要填补的个数
如果上数小于等于 0的个数的话就OK



# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here、
        cnt_zero = 0
        cnt_f_zero = 0
        MIN = 0xffff
        MAX = -0xffff
        for i in range(len(numbers)):
            if numbers[i] == 0:
                cnt_zero += 1
                continue
            if i < len(numbers)-1:
                if numbers[i] != 0 and numbers[i+1] == numbers[i]:
                    return False
            if numbers[i] != 0:
                cnt_f_zero += 1
                if numbers[i] > MAX:MAX = numbers[i]
                if numbers[i] < MIN:MIN = numbers[i]
        temp = MAX - MIN + 1 - cnt_f_zero
        if temp < 0 or temp > cnt_zero:
            return False
        return True