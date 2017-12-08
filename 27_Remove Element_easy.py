'''
27. Remove Element 
2017.12.8
'''
#这道题测评系统有问题
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #为什么测试样例返回的是数组？
        if len(nums)==0:
            return nums
        before=0
        behind=len(nums)-1
        while before != behind:
            if nums[before] == val:
                temp=nums[before]
                nums[before]=nums[behind]
                nums[behind]=temp
                behind-=1
            else:
                before+=1
        return before+1
        

_______________________________________
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #为什么测试样例返回的是数组？
        while val in nums:
            nums.remove(val)
        return(len(nums))