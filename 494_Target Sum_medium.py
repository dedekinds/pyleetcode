'''
494. Target Sum
2018.2.27
'''
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        请合"416. Partition Equal Subset Sum"来看
        这里的dp表示的是第i轮时候和为j的组合数
        http://blog.csdn.net/xiaoxiaoley/article/details/78968852
        
        target=S+sum(nums)
        if sum(nums)<S or target%2==1:return 0
        target=int(target/2)
        
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j]=dp[j]+dp[j-nums[i]]
        return dp[target]
                
        
        
        
        
    #——————————————————————————————————
    #暴力递归TLE
        self.ans=0
        def dfs(Sum,cnt):
            if cnt==len(nums):
                if Sum==S:
                    self.ans+=1
                return 
            dfs(Sum-nums[cnt],cnt+1)
            dfs(Sum+nums[cnt],cnt+1)
        dfs(0,0)
        return self.ans
       
