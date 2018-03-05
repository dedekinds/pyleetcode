'''
795. Number of Subarrays with Bounded Maximum
2018.3.5
'''
————————O(n)的DP———————————
class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        prev=-1
        ans=0
        dp=0
        for i in range(len(A)):
            if A[i]<L and i>0:
                ans+=dp
            if A[i]>R:
                dp=0
                prev=i
            if L<=A[i]<=R:
                dp=i-prev
                ans+=dp
        return ans
'''
1.将数组A按A[i]划分出等价类，即以A[i]为结尾的连续数组分类

2.dp[i]表示的是以A[i]为结尾的数组中，满足题目条件的数量（即最大值在[L,R]）

3.1:若A[i]<L，那么看A[i-1]，那么以A[i-1]为结尾的数组带上A[i]无伤大雅，反正A[i]不在[L,R]内，即dp[i]=dp[i-1]，注意到i=0时特殊处理一下（这里放在3.3处理）
3.2:若A[i]>R，那么说明不满足条件，dp=0，由连续性后面的数组不可能穿过A[i]，所以设置一个新的起点prev=i
3.3:若L<=A[i]<=R，那么由连续性，dp新增加的数组只有A[prev+1]~A[i],A[prev+2]~A[i],...,A[i]~A[i],共i-prev个，dp=i-prev

'''

————————O(n^2)的DP，导致TLE————————————
class Solution(object):
    def check(self,nums,L,R):
        temp=max(nums)
        if temp<=R and temp>=L:
            return 1
        else:
            return 0
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        f=[[0]*len(A) for x in range(len(A))]
        for i in range(len(A)):
            f[i][i]=self.check([A[i]],L,R)
        
        
        for k in range(1,len(A)):
            for j in range(k,len(A)):
                f[j-k][j]=f[j-k+1][j]+f[j-k][j-1]-f[j-k+1][j-1]+self.check(A[(j-k):(j+1)],L,R)
                #f[i][j]=f[i+1][j]+f[i][j-1]-f[i+1][j-1]+self.check(A[i:(j+1)],L,R)
        return f[0][len(A)-1]