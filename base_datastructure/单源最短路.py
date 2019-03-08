Bellman
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        d = [float('inf')]*N
        d[K - 1] = 0
        for i in range(N-1):
            for edge in times:
                if d[edge[1]-1] > d[edge[0]-1] + edge[2]:
                    d[edge[1]-1] = d[edge[0]-1] + edge[2]
        if sum(d) < float('inf'):return max(d)
        return -1


____________________________________________
import collections
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        d = [float('inf')]*N
        d[K - 1] = 0
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        Q = set(range(1,N+1))
        while Q:
            min_node = -1
            min_dist = float('inf')
            for temp in Q:
                if d[temp-1]<min_dist:
                    min_node = temp
                    min_dist = d[temp-1]
            if min_node == -1:return -1
            
            Q.remove(min_node)
            for nei,w in graph[min_node]:
                if d[nei-1] > d[min_node-1] + w:
                    d[nei-1] = d[min_node-1] + w
        return max(d)
____________________________________________
import collections
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        d = [float('inf')]*N
        d[K-1] = 0
        Q = [K]
        while Q:
            temp = Q.pop(0)
            for v,w in graph[temp]:
                if d[v-1] > d[temp-1] + w:
                    d[v-1] = d[temp-1] + w
                    if v not in Q:
                        Q.append(v)
        if max(d) < float('inf'):return max(d)
        return -1