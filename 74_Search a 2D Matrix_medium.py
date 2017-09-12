'''74. Search a 2D Matrix 
   2017.9.12
'''
先压平矩阵，然后用二分法

class Solution(object):
    def binsearch(self,nums,target):
        left=0
        right=len(nums)-1
        if nums[left]==target:
            return True
        if nums[right]==target:
            return True
        while left+1<right:
            mid=(left+right)>>1
            if nums[mid]>target:
                right=mid
            elif nums[mid]<target:
                left=mid
            else:
                return True
        return False
    
    def searchMatrix(self, matrix, target):
        if len(matrix)==0:
            return False
        if len(matrix[0])==0:
            return False
        return self.binsearch(sum(matrix,[]),target)
