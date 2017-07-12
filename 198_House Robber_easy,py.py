'''198. House Robber  
   2017.7.12

'''
假设有个数组是[a1,a2,...,an]，假设前k个数的结果是ans[k]，
那么有ans[n]=max{an+ans[n-2],ans[n-1]}

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #a1,a2,...,an
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