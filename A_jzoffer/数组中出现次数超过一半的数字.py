
# -*- coding:utf-8 -*-
import collections
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) <= 0:
            return 0
        temp = collections.Counter(numbers)
        mid = int(len(numbers)/2)
        for l,v in temp.items():
            if v > mid:return l
        return 0



——————————————————————————————————————————————————
# -*- coding:utf-8 -*-
如果一定存在的话，这样做应该是可以的，用更快速排序寻找中位数，若存在性都不能保证的话，还要花时间在检查是不是
中位数，那么仍然是O(n)的时间

class Solution:
    def partition(self,array,l,r):
        x = array[r]
        i = l - 1
        for j in range(l,r):
            if array[j] <= x:
                array[i],array[j] = array[j],array[i]
        array[i+1],array[r] = array[r],array[i+1]
        return i+1
    
    def find_max_k(self,array,k):
        left = 0
        right = len(array)-1
        index = self.partition(array,left,right)
        while index != k:
            if index > k:
                right = index - 1
                index = self.partition(array,left,right)
            else:
                left = index + 1
                index = self.partition(array,left,right)
        return array[index]
                
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) <= 0:
            return 0
        MID = self.find_max_k(numbers,int(len(numbers)/2))
        return numbers