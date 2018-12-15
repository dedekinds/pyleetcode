# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def depth_tree(self,root):
        if not root:return 0
        left = self.depth_tree(root.left)
        right = self.depth_tree(root.right)
        return [1+left,1+right][left < right]
        
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:return True
        if abs(self.depth_tree(pRoot.left) - self.depth_tree(pRoot.right)) > 1:
            return False
        return True