'''
684. Redundant Connection
2018.3.1
'''
from operator import *
from functools import reduce


#并查集
#https://zhuanlan.zhihu.com/p/29035169
#https://segmentfault.com/a/1190000004023326
#利用并查集来找到连通图中的环

class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        #初始化parent
        parent=list(range(1+max(sum(edges,[]))))
        #[[1,2],[1,3],[2,3]]→[0, 1, 2, 3]
        #自映射 parent[i]=i
        def find_root(x):
            while parent[x]!=x:x=parent[x]#若没到自映射，说明还没到根节点
            return x
        for s,t in edges:
            ps,pt=find_root(s),find_root(t)
            if ps==pt:return [s,t]
            parent[ps]=pt
            
————————————————————————————————————————————————————————————————————————

压缩路径 递归式 并查集
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = (1+max(sum(edges,[])))*[-1]
        
        def find_root(x):
            if parent[x] == -1:return x
            parent[x] = find_root(parent[x])
            return parent[x]
        
        for u,v in edges:
            pu , pv = find_root(u),find_root(v)
            if pu == pv:return [u,v]
            parent[pu] = pv
        
        
