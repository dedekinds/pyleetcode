
'''
125. Valid Palindrome
2017.12.26
'''
双指针，只考虑数字或者字母

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=0
        right=len(s)-1
        
        while left < right:
            #zuo
            while left<right and not s[left].isalnum():
                left+=1
            #you
            while left<right and not s[right].isalnum():
                right-=1
                
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True

