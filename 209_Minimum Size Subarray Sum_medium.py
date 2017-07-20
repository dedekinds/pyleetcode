
'''209. Minimum Size Subarray Sum 
   2017.7.20

'''

滑块法O(n+n/2+n/3+...+n/n)~O(nlogn)~~~TLE
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
            
            