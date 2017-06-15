'''342. Power of Four 
   2017.6.15
'''


如果是对于素数的幂次，可以采用一种巧妙的办法：
先算出3^x<pow(2,31)-1=2147483647
然后

#太强了
class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0


对于2的幂次：
可以考虑位运算
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
       