'''
504. Base 7 
2017.11.25
'''
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return str(0)
        temp=abs(num)
        ans=''
        while temp:
            ans+=str(temp%7)
            temp=int(temp/7)
        if num>0:
            return ans[::-1]
        else:
            return '-'+ans[::-1]
        
        