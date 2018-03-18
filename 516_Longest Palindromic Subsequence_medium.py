'''
516. Longest Palindromic Subsequence
2018.3.18
'''
class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        dp = [[0]*size for x in range(size)]
        for i in range(size):
            dp[i][i] = 1
            
        for i in range(size-1,-1,-1):
            #注意转移方程的方向是左下角，所以i需要从底部开始，即反向
            for j in range(i+1,size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j] ,dp[i][j-1])
        return dp[0][size-1]