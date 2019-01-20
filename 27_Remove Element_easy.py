'''
27. Remove Element 
2017.12.8
'''
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        first = 0
        second = len(nums)
        while first < second:
            if nums[first] == val:
                nums[first] = nums[second-1]
                second -= 1
            else:
                first += 1
        return first
    

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