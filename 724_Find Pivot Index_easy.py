'''
724. Find Pivot Index 
2017.12.1
'''
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=sum(nums)
        sum_left=0
        for x in range(len(nums)):
            if sum_left*2+nums[x]==temp:
                return x
            sum_left+=nums[x]
        return -1
            
            