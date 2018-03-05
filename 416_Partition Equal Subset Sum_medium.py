其实这就是coin change问题啊！
http://blog.csdn.net/qq_23997101/article/details/74009845
——————————————————————————————————————
'''
416. Partition Equal Subset Sum
2018.2.27
'''
class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #https://zhuanlan.zhihu.com/p/32364476?utm_source=qq&utm_medium=social
        '''
        这里的dp[j]表示的是第i轮的时候，是否有和为j的数组
        
        1.从前往后是错的：本来的DP方程应该是dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i]]，当压缩到一维的时候，dp[j]表示的是第i轮和为j的组合数，dp[j]（第i 轮)=dp[j]（第i-1轮) or dp[j-nums[i]]（第i-1轮)；注意到，大的dp由两个小的dp产生，如果从前往后的话，那么小的dp会率先进入第i轮，不满足（第i轮)=（第i-1轮)+（第i-1轮)的形式；

        2.从后往前是对的，注意到外层循环已经保证了到了第i轮的时候，所有i-1轮的dp都已经算出来了，由于大的dp由小的dp得到（dp[j]=dp[j] or dp[j-nums[i]]），在从后往前计算的话，小的DP的更新和大的DP无关，防止了混乱（实际上和第1点是一样的）
        '''
        
        
        Sum=sum(nums)
        if Sum %2==1:return False
        Sum=int(Sum/2)
        
        dp=[False]*(Sum+1)
        dp[0]=True
        
        for i in range(len(nums)):
            for j in range(Sum,nums[i]-1,-1):
                dp[j]=(dp[j] or dp[j-nums[i]])
        return dp[Sum]
