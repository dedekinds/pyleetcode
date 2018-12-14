# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:return 0
        height_left = self.TreeDepth(pRoot.left)
        height_right = self.TreeDepth(pRoot.right)
        return [height_left+1,height_right+1][height_left < height_right]



