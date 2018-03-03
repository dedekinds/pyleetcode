'''
525. Contiguous Array
2018.3.3
'''
class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
        count=0
        temp={0:0}#记录count中的值出现的最小index
        ans=0
        for index,num in enumerate(nums,1):
            if num==0:count-=1
            else:count+=1
            
            if count in temp:
                ans=max(ans,index-temp[count])
            else:
                temp[count]=index
        return ans
                
                