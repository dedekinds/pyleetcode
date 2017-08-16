'''560. Subarray Sum Equals K 
   2017.8.16
'''

————————————————————————————————————————
O(n2)的暴力，遍历每一个nums元，再遍历其后的所有元
光荣TLE
class Solution(object):
    def subarraySum(self, nums, k):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            if nums[0]==k:
                return 1
            else:
                return 0 
        ans=0
        for temp in range(len(nums)):
            Sum=nums[temp]
            if Sum==k:
                ans+=1
            while temp<len(nums)-1:
                temp+=1
                Sum+=nums[temp]
                if Sum==k:
                    ans+=1
        return ans




————————————————————————————————————————
下面的方法是用一个“动态的双指针”，利用“介值定理”来完成计算，之前好像也有道题可以这么
做，就是若sum<k那么右指针++，直到sum>k，同理若sum>k，那么左指针++，如此类推
不过没想到，这样的方法仅仅对正整数有效而已
对于比如[-1,-1,1] k=0这样的就不行，因为左指针++起不到降的作用，反而升
-----

那么是不是可以找到最大值然后大家都加上那个最小值呢？那k怎么变化，并不是直接加最
大值。。O(n)

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            if nums[0]==k:
                return 1
            else:
                return 0
        temp=min(nums)
        for x in nums:
        	x+=temp+1
        k+=temp+1


        left=0
        right=0
        Sum=nums[0]
        ans=0
        while left<=len(nums)-1 and right<=len(nums)-1:  
            if Sum==k:
                right+=1
                ans+=1
                if right<len(nums):
                    Sum+=nums[right]
                continue
            
            if left==right:
                right+=1
                if right<len(nums):
                    Sum+=nums[right]
                continue
            
            if Sum<k:
                while Sum<k and right<len(nums):
                    right+=1
                    if right<len(nums):
                        Sum+=nums[right]
                continue
                
            if Sum>k:
                while Sum>k and left<right:
                    Sum-=nums[left]
                    left+=1
                continue
        return ans