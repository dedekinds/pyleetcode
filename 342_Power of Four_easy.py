'''342. Power of Four 
   2017.6.15
'''
______________________
数值方法：
import math
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type num: int
        :rtype: bool
        """
        if n<=0:
            return False
        else:
            temp=int(0.5+math.log(n,4))
            if abs(temp-math.log(n,4))<0.0001:
                return True
            else:
                return False
_____________________
防溢出法
return num in set([4**0, 4**1, 4**2, 4**3, 4**4, 4**5, 4**6, 4**7, 4**8, 4**9, 4**10, 4**11, 4**12, 4**13, 4**14, 4**15]

————————————————————————————————————————
是2的幂次，然后bin(n).count(0)是偶数次的
def isPowerOfFour(self, num):
    return (num.bit_length()%2==1 and num & (num-1) == 0)



    
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
       