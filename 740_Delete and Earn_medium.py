'''
740. Delete and Earn
2018.3.2
'''
#https://leetcode.com/problems/delete-and-earn/discuss/109871/Awesome-Python-4-liner-with-explanation-Reduce-to-House-Robbers-Question
#将问题转换为robber house问题
class Solution(object):
    def rob(self,house):
        if len(house)==1:
            return house[0]
        if len(house)==2:
            return max(house[0],house[1])
        ans=[house[0],max(house[0],house[1])]
        for x in range(2,len(house)):
            ans.append(max(house[x]+ans[x-2],ans[x-1]))
        return ans[-1]
        
        
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        house=[0]*(1+max(nums))
        for x in nums:
            house[x]+=x
        return self.rob(house)
            