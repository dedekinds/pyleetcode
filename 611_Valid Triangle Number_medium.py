'''
611. Valid Triangle Number
2018.2.27
'''
class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        先对数组进行排序
        然后从小到大遍历最小的边，另外用双指针表达另外两条边
        
        nums.sort()
        ans=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                continue
            k=i+2
            for j in range(i+1,len(nums)-1):
                while k<len(nums) and nums[i]+nums[j]>nums[k]:k+=1
                ans+=k-j-1
        return ans
        