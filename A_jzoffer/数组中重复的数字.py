# -*- coding:utf-8 -*-
'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，
但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。 
'''
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
     
    def duplicate(self, numbers, duplication):
        length = len(numbers)
        if length == 0:return False
        i = 0
        while (i < length):
            while(1):
                a = numbers[i]
                b = numbers[numbers[i]]
                if a == i:
                    i += 1
                    break
                else:
                    if a == b:
                        duplication[0] = numbers[i]
                        return True
                    else:
                        numbers[i],numbers[a] = b,a#这里numbers[a]不能写成numbers[numbers[i]]
                        continue
        return False