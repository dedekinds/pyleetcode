'''96. Unique Binary Search Trees 
   2017.8.14
'''

结果是卡塔兰数：http://blog.csdn.net/u010582082/article/details/69569237?locationNum=7&fps=1
import math
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return math.factorial(2*n)/math.factorial(n)/math.factorial(n+1)
        