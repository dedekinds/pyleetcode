'''357. Count Numbers with Unique Digits 
   2017.6.10
   39ms
'''
def countunique(n):
    temp=9
    for x in range(n-1):
        temp=temp*(9-x)#纯数学排列组合问题啊妈个鸡，O(n)遍历绝壁TLE，直接考虑不重复的数
        #3~9位数的时候，实际上就是9*9*8*...
    return temp
    
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        if n==1:
            return 10
        if n>=10:
            return 8877691#大于10由抽屉原理，必有重复的10位数
        ans=0
        for x in range(n):
            ans+=countunique(x+1)
        return ans+1