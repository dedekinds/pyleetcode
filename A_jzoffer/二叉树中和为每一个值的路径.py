巧妙的递归

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left,expectNumber - root.val)
        right = self.FindPath(root.right,expectNumber - root.val)
        for temp in left+right:
            res.append([root.val] + temp)
        return res
            
            