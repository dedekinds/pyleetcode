'''
718. Maximum Length of Repeated Subarray
2018.3.13
'''

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m = len(A)
        n = len(B)
        ans = 0
        dp = [0]*(n+1)#这里m+1/n+1 的原因是防止i j=0时候，dp[-1]，所以加一行一列
        for i in range(m):
            temp = [0]*(n+1)
            for j in range(n):
                if A[i] == B[j]:
                    temp[j] = dp[j-1]+1
                ans = max(ans,temp[j])
            dp = temp
        return ans
        
        
        
        #—————————————TLE——————————————————————————————————————————————————————————————————
        #dp[i][j]表示以A的第i个和B的j个结尾的最长公共子串的长度
        m = len(A)
        n = len(B)
        ans = 0
        dp = [[0]*(m+1) for x in range(n+1)]#这里m+1/n+1 的原因是防止i j=0时候，dp[-1][-1]，所以加一行一列
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1 
                else:
                    dp[i][j] = 0
                ans = max(ans,dp[i][j])
        return ans