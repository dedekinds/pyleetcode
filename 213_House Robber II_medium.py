'''
213. House Robber II
2018.3.1
'''
class Solution(object):
    def last_rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        else:
            ans=[nums[0],max(nums[0],nums[1])]
            for x in range(2,len(nums)):
                ans.append(max(nums[x]+ans[x-2],ans[x-1]))
        return ans[-1]
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        return max(self.last_rob(nums[1:]),self.last_rob(nums[:-1]))
        