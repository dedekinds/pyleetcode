约瑟夫环推导递推数学公式

# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0 or m <= 0:
            return -1
        res = [0] * (n+1)
        for i in range(1,n+1):
            res [i] = (res[i-1] + m) % i
        return res[-1]