'''
238. Product of Array Except Self
2018.2.22
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #不允许使用除法
        #http://bookshadow.com/weblog/2015/07/16/leetcode-product-array-except-self/
        #output[i]=x[0]*x[1]...x[i-1]*x[i+1]*x[i+2]*...x[n-1]
        output=[1]*len(nums)
        
        left=1
        for i in range(len(nums)-1):
            left*=nums[i]
            output[i+1]*=left
        right=1
        
        for i in range(len(nums)-1,0,-1):
            right*=nums[i]
            output[i-1]*=right
        return output
        