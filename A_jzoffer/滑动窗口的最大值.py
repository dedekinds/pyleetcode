# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        res = []
        maxindex = []
        if len(num) <= 0 or size <=0 or len(num) < size:
            return res 
        for i in range(len(num)):
            if maxindex and i - maxindex[0] >= size:
                maxindex.pop(0)
            while maxindex and num[i] > num[maxindex[-1]]:
                maxindex.pop()
            maxindex.append(i)
            if i >= size - 1 :
                res.append(num[maxindex[0]])
        return res
        

https://blog.csdn.net/qq_20141867/article/details/81088705
https://blog.csdn.net/u010429424/article/details/73692248