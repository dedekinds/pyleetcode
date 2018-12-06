在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。 

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0:
            return False
        if len(array[0]) == 0:
            return False
        i = len(array)-1
        j = 0
        length =len(array[0])
        while(i >= 0 and j < length):
            test = array[i][j]
            if target > test:
                j += 1
                continue
            if target < test:
                i -= 1
                continue
            if target == test:
                return True
        return False
       