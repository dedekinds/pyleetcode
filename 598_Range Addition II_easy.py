'''
598. Range Addition II 
2017.11.13
'''
实际上和m*n几乎没关，完全是找ops第一项和第二项中的最小值的乘积（overlap
class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:#对于[]不能用if ops is None:   要用if not ops:
            return m*n
        return min(temp[0] for temp in ops)*min(temp[1] for temp in ops)