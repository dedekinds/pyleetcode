消耗空间的方法，否则要按照原来的顺序的话可能要 O(n2)

# -*- coding:utf-8 -*-
from collections import deque
class Solution:
    def reOrderArray(self, array):
        # write code here
        Q = deque()
        length = len(array)
        for i in range(length):
            if array[i]%2 == 0:
                Q.append(array[i])
            if array[length - i -1] %2 != 0:
                Q.appendleft(array[length - i - 1])
        return list(Q)
