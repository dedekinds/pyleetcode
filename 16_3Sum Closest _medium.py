'''16. 3Sum Closest 
   2017.6.22
   169ms
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dis=66666666666666
        ans=23333333333333
        nums=sorted(nums)
        for x in range(len(nums)):
            if x!=0 and nums[x]==nums[x-1]:
                continue
            temp=nums[x]
            left=x+1
            right=len(nums)-1
            while(left<right):
                #print(nums[x],nums[left],nums[right])
                dis=abs(ans-target)
                if abs(nums[left]+nums[right]+nums[x]-target)<dis:
                    ans=nums[left]+nums[right]+nums[x]
                    dis=abs(ans-target)
                #print('ans=',ans,'dis=',dis)
                if nums[left]+nums[right]+nums[x]==target:
                    return nums[left]+nums[right]+nums[x]
                if nums[left]+nums[right]>target-nums[x]:
                    right-=1
                elif nums[left]+nums[right]<target-nums[x]:#这里要用elif如果是if是错的，会使得上下两句都会运行，跳步
                    left+=1
        return ans