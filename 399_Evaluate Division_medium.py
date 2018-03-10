'''
399. Evaluate Division
2018.3.10
'''
import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        建立一张二维的列表，初始化所有可能的节点，然后遍历queries去寻找就好了
        """
        g=collections.defaultdict(lambda: collections.defaultdict(int))#二维列表
        for (a,b),v in zip(equations,values):
            g[a][b] = v
            g[b][a] = 1.0/v
        for k in g:
            g[k][k] = 1.0
            for m in g:
                for n in g:
                    if g[m][k] and g[k][n]:
                        g[m][n] = g[m][k]*g[k][n]
        
        
        ans=[]
        for temp in queries:
            ans.append(g[temp[0]][temp[1]] if g[temp[0]][temp[1]] else -1.0)
        return ans