
'''
9. Palindrome Number
2017.12.17
'''
回文数双指针
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=str(x)
        left=0
        right=len(temp)-1
        while left<=right:
            if temp[left]!=temp[right]:
                return False
            else:
                left+=1
                right-=1   
        return True
