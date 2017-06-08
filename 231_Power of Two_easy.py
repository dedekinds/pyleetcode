'''231. Power of Two 
   2017.6.8

'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        return n&(n-1)==0
        #100....0减一后为01111..1，做&运算恰为0，那么其他数会不会这样呢？显然不会，只要中间有个1就会GG
