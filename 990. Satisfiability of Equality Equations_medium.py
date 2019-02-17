将==的字母构成一个图然后，再寻找所有!=的u,v如果在图中能u->v连通的话
说明是矛盾的！
同理用并查集能检查图的连通性

from collections import defaultdict
class Solution(object):
    def dfs(self,source,dest,adj):
        q = [source]
        vist = set()
        vist.add(source)
        while q:
            u = q.pop(0)
            if u == dest:
                return True
            for v in adj[u]:
                if v not in vist:
                    vist.add(v)
                    q.append(v)
        return False
        
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        adj = defaultdict(list)
        for eq in equations:
            tmp = eq.split('==')
            if len(tmp) == 2:
                u,v = tmp
                adj[u].append(v)
                adj[v].append(u)
                
        for eq in equations:
            tmp = eq.split('!=')
            if len(tmp) == 2:
                u,v = tmp
                if self.dfs(u,v,adj):
                    return False
        return True
            ——————————————————————————————————————————————————————————————————
并查集方法
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        def find_root(x):
            if parent[x] != x:
                parent[x] = find_root(parent[x])
            return parent[x]
        parent = {char: char for char in string.ascii_lowercase}
        
        for a,b,c,d in equations:
            if b == '=':
                parent[find_root(a)] = parent[find_root(d)]
        for a,b,c,d in equations:
            if b == '!':
                if find_root(a) == find_root(d):
                    return False
        return True