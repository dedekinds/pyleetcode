'''
414. Third Maximum Number 
2018.1.2
'''
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=b=c=-0xffffffff
        for x in nums:
            if x>a:
                a,b,c=x,a,b
            elif a>x>b:
                b,c=x,b
            elif b>x>c:
                c=x
        return c if c!=-0xffffffff else a
        