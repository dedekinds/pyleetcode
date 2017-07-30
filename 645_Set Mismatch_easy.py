'''645. Set Mismatch 
   2017.7.30
'''
class Solution(object):
    def findErrorNums(self, nums):
        ans=[]
        temp=[0]*len(nums)
        for x in range(len(nums)):
            if temp[nums[x]-1]==1:
                ans.append(nums[x])
            else:temp[nums[x]-1]+=1
        ans.append(int(ans[0]+len(nums)*(len(nums)+1)/2-sum(nums)))
        return ans
        