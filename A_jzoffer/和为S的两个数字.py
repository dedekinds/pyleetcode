# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        left  =  0
        right = len(array)-1
        while (left < right):
            if array[left] + array[right] > tsum:
                right -= 1
                continue
            if array[left] + array[right] < tsum:
                left += 1
                continue
            if array[left] + array[right] == tsum:
                return [array[left],array[right]]
                
        return []