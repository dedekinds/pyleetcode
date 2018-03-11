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
    
    ————————————————————————————————————————————————————————————————————————————————————————
    改用BFS写
    
import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def bfs(q,graph):
            start ,end = q

            if start not in graph or end not in graph:
                return -1.0
            
            temp = collections.deque([ (start,1.0) ])
            
            visited = set()
            while temp:#队列
                front ,cur_product = temp.popleft()
                if front == end:
                    return cur_product
                visited.add(front)
                for node in graph[front]:
                    if node not in visited:
                        temp.append( (node,cur_product*graph[front][node]) )
            return -1.0
                

                
        graph = collections.defaultdict(lambda:collections.defaultdict(int))
        for (m,n),v in zip(equations,values):
            graph[m][n] = v
            graph[n][m] = 1.0/v
        
        return [bfs(q,graph) for q in queries]
