
'''209. Minimum Size Subarray Sum 
   2017.7.20

'''
这是一种动态的two pointer，很有意思，首先先right变大，使得总和超过s，然后不断地减少left
，使得和变小，直到小于s，此时再扩大right，如此下去，
，而且，复杂度可以说明是O(n)

显然这种方法不会遍历所有的sum>=s的情况，但是如果没有遍历到的话，说明在这种方法下
肯定存在更短的情况，不管怎么样可以说明最小情况一定会被包含在里面，因为我们
可以假设right到达最优解的右边，由我们的算法，left一定会压缩到可能压缩的最好情况

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=0
        sum_num=0
        length=len(nums)
        ans=666666
        while right<length:
            while right<length and sum_num<s:
                sum_num+=nums[right]
                right+=1
            while left<right and sum_num>=s:
                ans=min(ans,right-left)
                print(ans)
                sum_num-=nums[left]
                left+=1
        if ans==666666:return 0
        else:return ans




________________________________________________
暴力滑块法O(n+n/2+n/3+...+n/n)~O(nlogn)~~~TLE
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans=666666
        for n in range(1,len(nums)+1):
            for m in range(0,len(nums)-n+1):
                #print(ans)
                if sum(nums[m:m+n])>=s:
                    return n
        return 0
            
            