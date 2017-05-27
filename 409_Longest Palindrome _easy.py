'''409. Longest Palindrome 
   2017.5.27
   55ms
   beats 48.94%
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        A=set(s)
        single=0
        ans=0
        for x in A:
            temp=s.count(x)
            if temp%2==0:
                ans=ans+temp
            else:
                ans=ans+temp-1
                single=1
        return ans+single
'''
'''
