
'''
643. Maximum Average Subarray I 
2017.12.13
'''
连续k和的套路
class Solution:
    def findMaxAverage(self, nums, k):
    	#O(n+k)
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        temp=[0]
        for x in range(len(nums)):
            temp.append(temp[-1]+nums[x])
        ans=max(temp[x+k]-temp[x] for x in range(len(nums)-k+1))
        return ans/k
        
        
        '''
        #O(nk)
        tempmax=-0xffffffff
        for x in range(len(nums)-k+1):
            temp=sum(nums[x:(x+k)])/k
            if temp>=tempmax:
                tempmax=temp
        return tempmax       
        '''

        