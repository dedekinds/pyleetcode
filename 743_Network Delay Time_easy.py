
实际上就是单源最短路问题首先是给出Bellman算法：
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        #Bellman
        d = [float('inf')] * N
        d[K-1] = 0
        for i in range(N - 1):
            for edge in times:
                if d[edge[1]-1] > d[edge[0]-1] + edge[2]:
                    d[edge[1]-1] = d[edge[0]-1] + edge[2]
        if sum(d) < float('inf'):return max(d)
        else:return -1

__________________________________________________________
class Solution:
    def networkDelayTime(self, times, N, K):
        #Dijkstra's algorithm  Basic Implementation
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        d = [float('inf')] * N
        Q = set(range(1,N+1))
        d[K-1] = 0
        
        while Q:
            min_node = -1
            min_u = float('inf')
            for temp in Q:
                if d[temp-1] < min_u:
                    min_u = d[temp - 1]
                    min_node = temp
            if min_node == -1:return -1
            
            Q.remove(min_node)
            for nei,w in graph[min_node]:
                if d[nei-1] > d[min_node-1] + w:
                    d[nei-1] = d[min_node-1] + w
        
        return max(d)
______________________________________________
import heapq
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        #Dijkstra's algorithm  heap

    
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        S = {}
        Q = [(0,K)]
        while Q:
            dist,node = heapq.heappop(Q)
            if node in S:continue #反正较小的在前面
            
            S[node] = dist
            for v,w in graph[node]:
                if v not in S:
                    heapq.heappush(Q,(dist + w,v))
        if len(S) == N:
            return max(S.values())
        else:return -1
                
                
                
                
            