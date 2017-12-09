'''
257. Binary Tree Paths 
2017.12.9
'''
深度优先搜索
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        self.ans=[]
        def travel(root,path):
            if root.left is None and root.right is None:
                self.ans.append(path)
            if root.left:
                travel(root.left,path+'->'+str(root.left.val))
            if root.right:
                travel(root.right,path+'->'+str(root.right.val))
        
        travel(root,str(root.val))
        return self.ans
