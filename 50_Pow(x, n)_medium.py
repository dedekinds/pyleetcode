class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:return 1/self.myPow(x,-n)
        if n == 1:return x
        if n == 0:return 1
        
        half = self.myPow(x,n//2)
        if n%2 == 0:
            return half*half
        else:
            return x*half*half

_________________________________________
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

迭代版