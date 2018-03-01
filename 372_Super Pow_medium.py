'''
372. Super Pow
2018.3.1
'''
class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        #http://blog.csdn.net/ltyqljhwcm/article/details/53043646
        #快速幂取模
        #O(log2 n)
        B=int(''.join(map(str,b)))
        ans=1
        A=a
        while B!=0:
            if B&1: ans=(ans*A)%1337
            B>>=1
            A=(A*A)%1337
        return ans
        