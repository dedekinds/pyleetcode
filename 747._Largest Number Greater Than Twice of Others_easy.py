
'''
747. Largest Number Greater Than Twice of Others
2017.12.24
'''
纯暴力

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return -1
        maxnums=nums[0]
        index=0
        for x in range(len(nums)):
            if nums[x]>=maxnums:
                index=x
                maxnums=nums[x]
        nums=nums[:index]+nums[index+1:]
        #print(index)
        for x in nums:
            if maxnums<2*x:
                return -1
        return index