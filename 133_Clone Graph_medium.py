'''133. Clone Graph 
   2017.8.4
'''
用队列实现BFS
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
#用BFS试试
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return node
        ans=UndirectedGraphNode(node.label)
        ans_dict={node.label:ans}
        queue=[node]
        self.bfs(queue,ans_dict)
        return ans
    
    def bfs(self,queue,ans_dict):
        while queue:
            top=queue.pop()
            for x in top.neighbors:
                if x.label not in ans_dict:
                    temp=UndirectedGraphNode(x.label)
                    ans_dict[x.label]=temp
                    queue.insert(0,x)
                ans_dict[top.label].neighbors.append(ans_dict[x.label])
                
    '''   
用栈实现DFS
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return node
        ans=UndirectedGraphNode(node.label)#创建一个图
        #DFS
        ans_dict={node.label:ans}#用来判断是否被访问
        stack=[node]
        while stack:
            top=stack.pop()
            temp=ans_dict[top.label]#准备用来复制neighbors
            for x in top.neighbors:
                if x.label not in ans_dict:#如果没有被访问的话
                    ans_dict[x.label]=UndirectedGraphNode(x.label)
                    stack.append(x)
                temp.neighbors.append(ans_dict[x.label])
        return ans
'''

————————————————————————————————

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        queue = [node]
        # self.bfs(queue, dic)
        self.dfs(queue, dic)
        return nodeCopy
        
    def bfs(self, queue, dic):
        while queue:
            front = queue.pop()
            for neighbor in front.neighbors:
                if neighbor not in dic: 
                    # neighor not visited
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[front].neighbors.append(neighborCopy)
                    queue.insert(0, neighbor)
                else:
                    # neighbor visited
                    dic[front].neighbors.append(dic[neighbor])
                    
    def dfs(self, stack, dic):
        while stack:
            front = stack.pop()
            for neighbor in front.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[front].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[front].neighbors.append(dic[neighbor])

