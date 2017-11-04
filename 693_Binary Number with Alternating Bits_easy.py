'''
693. Binary Number with Alternating Bits 
2017.11.4
'''
分奇偶性，本身和本身移位相加+1如果是一种2的幂次的话则是相间
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%2==1:
            if 3*n==pow(2,len(bin(n))-1)-1:
                return True
            else:
                return False
        if n%2==0:
            if 3*n+1==pow(2,len(bin(n))-1)-1:
                return True
            else:
                return False