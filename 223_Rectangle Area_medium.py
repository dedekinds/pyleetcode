'''223. Rectangle Area 
   2017.8.23
'''
这个问题实际上只有两种情况，可以分析，如果相交的话那么相交矩形用
这里的表示法可以表示为：
(min(C,G),max(F,B))
(max(A,E),min(D,H))

如果不相交或者交点在边上则为0

这样的处理对于退化的矩形同样有效

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        return abs(C-A)*abs(D-B)+abs(G-E)*abs(H-F)-max(min(C,G)-max(A,E),0)*max(min(D,H)-max(F,B),0)
        
        
        
        
        
        '''
        if E<=C and H>=B and E>=A and H<=D:
            return abs(C-A)*abs(D-B)+abs(G-E)*abs(H-F)-abs(E-C)*abs(H-B)
        else:
            return abs(C-A)*abs(D-B)+abs(G-E)*abs(H-F)
        '''