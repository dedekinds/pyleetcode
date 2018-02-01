'''
565. Array Nesting
2018.2.2
'''
class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #遍历每一个点，访问过就变成-1，然后计算最长的圈
        def findcircle(index):
            cnt=0
            while nums[index]>=0:
                cnt+=1
                nextpoint=nums[index]
                nums[index]=-1
                index=nextpoint
            return cnt
        
        ans=0
        for x in range(len(nums)):
            if nums[x]>=0:
                ans=max(ans,findcircle(x))
        return ans
            
        