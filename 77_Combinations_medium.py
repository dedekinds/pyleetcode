
类似参考subset问题
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == k:return [[tmp for tmp in range(1,n+1)]]
        if k == 0:return [[]]
        with_n = self.combine(n-1,k-1)
        without_n = self.combine(n-1,k)
        
        for i in range(len(with_n)):
            with_n[i] = with_n[i] + [n]
        return with_n + without_n
            
        