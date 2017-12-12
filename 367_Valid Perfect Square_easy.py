'''
367. Valid Perfect Square 
2017.12.12
'''
二分法
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        left=0
        right=num
        while left+1<right:
            temp=(left+right)>>1
           # print(temp)
            if temp*temp>num:
                right=temp
            elif temp*temp<num:
                left=temp
            else:
                return True
        return False
