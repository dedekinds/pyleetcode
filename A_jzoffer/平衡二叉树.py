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
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)



        _________________________________________________
    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def depth_tree(self,root):
        if not root:return 0
        left = self.depth_tree(root.left)
        if left == -1:return -1
        right = self.depth_tree(root.right)
        if right == -1:return -1
        if abs(left - right)>1:return -1
        else:return max(left,right)+1
    
    def isBalanced(self, pRoot):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.depth_tree(pRoot) != -1