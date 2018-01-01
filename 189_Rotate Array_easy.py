
'''
189. Rotate Array
2018.1.1
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        
        '''
        while k:
            temp=nums.pop()
            nums.insert(0,temp)
            k=k-1
        '''

            
        nums[:] = nums[len(nums) - k: ] + nums[:len(nums) - k]