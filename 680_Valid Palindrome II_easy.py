
'''
680. Valid Palindrome II
2017.12.23
'''
如果发现不少回文，那么给一次机会把那个字符剔除
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ispalindrome=lambda s:s==s[::-1]
        conbination=lambda x,s: s[:x]+s[x+1:]
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return ispalindrome(conbination(left,s)) or ispalindrome(conbination(right,s))
            left+=1
            right-=1
        return True