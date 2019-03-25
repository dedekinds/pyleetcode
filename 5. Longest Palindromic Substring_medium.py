dp[i][j]表示字符在i-j之间的字符串是否是回文

dp[i][j] =
True  if i=j
True  if s[i]==s[i+1]
True  if s[i]==s[j] and dp[i-1][j+1]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        dp = [[False]*m for i in range(m)]
        maxval = -0xffffff
        ans=[-1,-1]
        for i in range(m):
            dp[i][i] = True
            if abs(i-i)>=maxval:
                ans[0],ans[1] = i,i
        for i in range(m-1):
            if s[i]==s[i+1]:
                dp[i+1][i] = True
                if abs(i+1-i)>=maxval:
                    ans[0],ans[1] = i,i+1
        for j in range(2,m):
            for i in range(j,m):
                dp[i][i-j] = (s[i]==s[i-j]) and dp[i-1][i-j+1]
                if dp[i][i-j] and j >=maxval:
                    ans[0],ans[1] = i-j,i
        return s[ans[0]:ans[1]+1]
        