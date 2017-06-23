'''18. 4Sum 
   2017.6.23
   169ms
'''




————————TLE————————
#思路是用两个for 再来里面两个指针夹逼一共是o(n2)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                #if j!=0 and nums[j]==nums[j-1]是否要这句呢？
                left=j+1
                right=len(nums)-1
                while(left<right):
                    if nums[i]+nums[j]+nums[left]+nums[right]==target:
                        temp=sorted([nums[i],nums[j],nums[left],nums[right]])
                        if temp not in ans:
                            ans.append(temp)
                        #temp=sorted([nums[i],nums[j],nums[left],nums[right]]   
                        right-=1
                        left+=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    if nums[left]+nums[right]+nums[i]+nums[j]>target:
                        right-=1
                    if nums[left]+nums[right]+nums[i]+nums[j]<target:
                        left+=1
        return ans