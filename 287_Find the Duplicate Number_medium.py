'''
287. Find the Duplicate Number
2018.2.7
'''
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #用以前的一篇博文http://blog.csdn.net/qq_23997101/article/details/49047133即可
        #先判断是否成环
        #然后判断环的起点
        #构造一个抽象的环,变换是nums
        
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break    
        new_pointer=0
        
        while True:
            slow=nums[slow]
            new_pointer=nums[new_pointer]
            if slow==new_pointer:
                return slow
