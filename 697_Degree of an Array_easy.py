'''
697. Degree of an Array 
2017.11.15
'''
分别保存元素的最小下标，最大下标，个数

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        indexmax={}
        indexmin={}
        numerical={}
        for index in range(len(nums)):
            if indexmin.get(nums[index],-1)==-1:
                indexmin[nums[index]]=index
                indexmax[nums[index]]=index
                numerical[nums[index]]=1
            else:
                indexmax[nums[index]]=index
                numerical[nums[index]]+=1
        degree=max(numerical.values())

        ans=len(nums)
        #for temp in numerical:
        for temp in set(nums):
            if numerical[temp] == degree:
                ans=min(ans,indexmax[temp]-indexmin[temp]+1)
        return ans
