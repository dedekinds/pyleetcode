'''
647. Palindromic Substrings
2018.1.25
'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #http://blog.csdn.net/lishichengyan/article/details/77103324
        dp=[[0]*len(s) for temp in range(len(s))]
        ans=0
        i=len(s)-1
        while i>=0:
            for j in range(i,len(s)):
                dp[i][j]=int( (s[i]==s[j]) and (j-i<3 or dp[i+1][j-1]) )
                if dp[i][j]:
                    ans+=1 
            i-=1
        return ans
                
