'''
674. Longest Continuous Increasing Subsequence 
2017.11.27
'''
直接遍历暴力O(n)
class Solution:
    def findLengthOfLCIS(self, nums):
        if len(nums)==0:
            return 0
        pointer=0
        length=len(nums)
        ans=1
        temp_ans=1
        while pointer<length-1:
            if nums[pointer]<nums[pointer+1]:
                temp_ans+=1
            else:
                temp_ans=1
            ans=max(ans,temp_ans)
            pointer+=1
        return ans 
