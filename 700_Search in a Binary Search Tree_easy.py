# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:return root
        pt = root
        while pt:
            if pt.val > val:
                pt = pt.left
                continue
            if pt.val < val:
                pt = pt.right
                continue
            if pt.val == val:
                return pt
        return None