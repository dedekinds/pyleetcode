'''650. 2 Keys Keyboard 
   2017.8.31
'''
做了一个猜想：
1.素数时候直接返回素数，这个显然
2.否则对n做分解,n=a*b，其中a为其非1的最小因子，然后ans[n]=ans[a]+(m-1)+1

import math
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 0
        ans=[0,0,2,3]
        for x in range(4,n+1):
            minfactor=1
            for temp in range(2,1+int(math.sqrt(x))):
                if x%temp==0:
                    minfactor=temp
                    break
            if minfactor==1:
                ans.append(x)
            else:
                ans.append(ans[int(x/minfactor)]+minfactor)
        return ans[n]