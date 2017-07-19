'''209. Minimum Size Subarray Sum 
   2017.7.19

'''
import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        for x in range(1,1+int(math.log(n,5)):
            sum+=int(n/pow(5,x))
        return sum