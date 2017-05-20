'''371_Sum of Two Integers 
   2017.5.20
   49ms
   beats 23.42%
'''
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)
        #http://blog.csdn.net/coder_orz/article/details/52034541
        #Python的整数不是固定的32位，所以需要做一些特殊的处理

'''
这样的办法对负数无效，但是在C++和JAVA是可以的
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        #http://blog.csdn.net/zhongjiekangping/article/details/6855864
        #直到不产生进位为止
        #x^y //执行加法
        #(x&y)<<1 //进位操作
        result=a^b
        while(a&b):
            b=(a&b)<<1
            a=result
            result=a^b
            print(result)
        return result
'''
递归
def getSum(self, a, b):
    def add(a, b): 
        if not a or not b:
            return a or b
        return add(a^b, (a&b) << 1)

    if a*b < 0: # assume a < 0, b > 0
        if a > 0:
            return self.getSum(b, a)
        if add(~a, 1) == b: # -a == b
            return 0
        if add(~a, 1) < b: # -a < b
            return add(~add(add(~a, 1), add(~b, 1)),1) # -add(-a, -b)

    return add(a, b) # a*b >= 0 or (-a) > b > 0 