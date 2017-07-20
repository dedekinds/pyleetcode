
'''637. Average of Levels in Binary Tree 
   2017.7.20

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
用层次遍历，其中中途用个新的tempQ代替一层的所有结点
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans=[]
        Q=[root]
        while Q:
            ans.append(1.0*sum([tree.val for tree in Q])/len(Q))
            tempQ=[]
            for x in Q:
                if x.left:
                    tempQ.append(x.left)
                if x.right:
                    tempQ.append(x.right)
            Q=tempQ
        return ans