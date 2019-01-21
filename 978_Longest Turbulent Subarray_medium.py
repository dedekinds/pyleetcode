class Solution:
    def maxTurbulenceSize(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        cnt = 0
        maxv = -0xffffffff
        for i in range(len(nums)-2):
            if (nums[i]-nums[i+1])*(nums[i+1]-nums[i+2]) < 0:
                cnt+= 1
            else:
                if cnt > maxv :
                    maxv = cnt
                cnt = 0
        if cnt > maxv:
            maxv = cnt
        return maxv+2