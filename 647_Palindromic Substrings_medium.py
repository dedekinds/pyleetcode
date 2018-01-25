'''
647. Palindromic Substrings
2018.1.25
'''
用队列快很多（一倍的样子
import collections
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #http://bookshadow.com/weblog/2017/07/24/leetcode-palindromic-substrings/
        temp=collections.deque((x,x) for x in range(len(s)))
        for x in range(len(s)-1):
            if s[x]==s[x+1]:
                temp.append((x,x+1))
        
        ans=0
        while temp:
            a,b=temp.popleft()
            ans+=1#一开始单个字母
            
            if a-1>=0 and b+1<len(s) and s[a-1]==s[b+1]:
                temp.append((a-1,b+1))
        return ans
_________________________________
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
                
