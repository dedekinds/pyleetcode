'''
486. Predict the Winner
2018.2.10
'''
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp=[[0]*len(nums) for x in range(len(nums))]#此时的dp表示在数组i,j之间能获得的最大的分值
        for x in range(len(nums)):
            dp[x][x]=nums[x]
        
        #注意dp的方向，是斜向下
        for i in range(1,len(nums)):
            for j in range(len(nums)-i):
                dp[j][j+i]=max( sum(nums[j:j+i+1])-dp[j+1][i+j], sum(nums[j:j+i+1])-dp[j][i+j-1] )
                #dp[i][j]=max( sum(i,j)-dp[i+1][j], sum(i,j)-dp[i][j-1]])
        return dp[0][len(nums)-1]>=sum(nums)-dp[0][len(nums)-1]

——————————————————————————————————————————————————————————
        #http://blog.csdn.net/starstar1992/article/details/60605888
        #这里的dp表示两者收益的差
        dp=dict()
        def solve(nums):
            if len(nums)<=1:
                return sum(nums)
            temp=tuple(nums)#这样的话可以放进dict里
            
            if temp in dp:
                return dp[temp]
            dp[temp]=max(nums[0]-solve(nums[1:]),nums[-1]-solve(nums[:-1]))
            return dp[temp]
        return solve(nums)>=0        
