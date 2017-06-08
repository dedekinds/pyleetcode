'''70. Climbing Stairs 
   2017.6.8

'''
import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #x+2y=n
        #的解的形式为x0+2k,y0-k，由非负性给出k的范围
        #直接算出1和2的数量，用有重复元素的不重复排列
        #元素表述：   a1,a1,...a1,   a2,a2,...a2,.......,an,an,...an
        #其中，a1的个数为N1,   a2的个数为N2,以此类推，总个数为M。
        #则可以证明不重复的排列种类的数目:   M!/(N1!*N2!*...*Nn!) 
        #k=n%2+1#k表示不定方程解的个数
        num=0
        if n%2==1:
            for x in [y for y in range(1,n+1) if y %2 ==1]:
                y=(n-x)/2
                num+=math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
        if n%2==0:
            for x in [y for y in range(0,n+1) if y %2 ==0]:
                y=(n-x)/2
                num+=math.factorial(x+y)/(math.factorial(x)*math.factorial(y))
        return int(num)