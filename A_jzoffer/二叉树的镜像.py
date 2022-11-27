# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        # write code here
        if not pRoot:
            return None
        left = self.Mirror(pRoot.left)
        right = self.Mirror(pRoot.right)
        pRoot.left = right
        pRoot.right = left
        return pRoot
            
