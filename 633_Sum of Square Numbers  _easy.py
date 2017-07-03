'''633. Sum of Square Numbers  
   2017.7.3

'''
神器：math.sqrt(121).is_integer()
_______________
import math
class Solution(object):
    def judgeSquareSum(self, c):
        for a in range(1+int(math.sqrt(c))):
            temp=c-a*a
            if abs(math.sqrt(temp)-int(math.sqrt(temp)+0.5))<0.000001:#完全卡这个精度了
                #print(a,math.sqrt(temp),c)
                return True
        return False

 _______利用2sum

 class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        maxs = 1
        while (maxs * maxs) < c :
            maxs +=1 
        
        
        lo = 0
        hi = maxs
        while lo <= hi:
            if ((lo * lo) + (hi * hi)) == c :
                return True
            if ((lo * lo) + (hi * hi)) < c :
                lo += 1
            if ((lo * lo) + (hi * hi)) > c :
                hi -= 1
        
        # Bruthe force until maxs O(n^2)
        # for i in range(1,maxs):
        #    for j in range(1,maxs):
        #        if c == (i*i + j*j):
        #            return True
        
        return False