class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        #dp[i] = dp[i-1]if s[i-1]!=0 + dp[i-2] if s[i-1:i+1] \in [9,26]
        
        if len(s)==0:return 0
        dp = [1] + [0]*len(s)
        for i in range(1,len(s)+1):
            dp[i] = [0,dp[i-1]][int(s[i-1])!=0] + [0,dp[i-2]][i>=2 and 10<= int(s[i-2:i]) <=26 ]
        return dp[-1]
        
        