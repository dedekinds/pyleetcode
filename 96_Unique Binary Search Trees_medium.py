'''96. Unique Binary Search Trees 
   2017.8.14
'''

结果是卡塔兰数：http://blog.csdn.net/u010582082/article/details/69569237?locationNum=7&fps=1
考虑卡塔兰数的递推式：
   ‘‘‘
是左子树的情况+右子树的情况

蔡某某 2018/3/17 15:22:24
左子树有j个结点

蔡某某 2018/3/17 15:22:35
右子树有i-j-1个
   ’’’

import math
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return math.factorial(2*n)/math.factorial(n)/math.factorial(n+1)
        
