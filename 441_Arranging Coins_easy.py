'''441. Arranging Coins 
   2017.7.5

'''
import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        sup=int((math.sqrt(1+8*n)-1)/2)
        inf=int((math.sqrt(9+8*n)-3)/2)
        for ans in range(inf,sup+1):
            if n-(ans+ans**2)/2<=ans:
                return ans