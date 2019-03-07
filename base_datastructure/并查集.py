# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:44:23 2019

@author: dedekinds
"""



def findRedundantConnection(edges):
    parent = [-1]*(1+max(sum(edges,[])))
    def find_root(x):
        if parent[x] == -1:return x
        parent[x] = find_root(parent[x])
        return parent[x]
    
    for u,v in edges:
        pu,pv = find_root(u),find_root(v)
        if pu == pv:return [u,v]
        parent[pu] = pv



edges = [[1,2],[1,3],[2,3]]
print(findRedundantConnection(edges))

