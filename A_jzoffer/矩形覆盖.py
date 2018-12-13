
'''
fibonacci数列构建递推式
'''

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        stack = [0]*number
        stack[0] = 1
        stack[1] = 2
        if number <= 2:
            return stack[number-1]
        for i in range(2,number):
            stack[i] = stack[i-1] + stack[i-2]
        return stack[-1]