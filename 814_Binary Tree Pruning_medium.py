# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasone(self,root):
        if not root:return False
        l = self.hasone(root.left)
        r = self.hasone(root.right)
        if not l:root.left = None
        if not r:root.right = None
        return root.val == 1 or l or r
        
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if self.hasone(root):return root
        else: return None
        