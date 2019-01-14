# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:return []
        s -= root.val
        if not root.right and not root.left and s == 0:
            return [[root.val]]
        left = self.pathSum(root.left,s)
        right = self.pathSum(root.right,s)
        res = []
        for temp in left+right:
            res.append([root.val]+temp)
        return res
        