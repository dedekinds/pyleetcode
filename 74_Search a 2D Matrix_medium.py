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
__________________________
最佳办法O(m+n)
考虑左下角或者右上角，以左下角为例
若左下角大于目标，那么目标在左下角上方的矩阵，若小于目标，那么再右方矩阵
一直考虑新矩阵的左下角即可
