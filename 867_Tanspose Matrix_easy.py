
*A的作用是解除列表
比如8*[[[1]]] = [[1]]
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*A))