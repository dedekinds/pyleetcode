'''
776. Split BST
2018.2.4
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return [root,root]
        if root.val==V:
            big=root.right
            root.right=None
            return [root,big]
        elif root.val<V:
            small,big=self.splitBST(root.right,V)
            root.right=small
            return [root,big]
        elif root.val>V:
            small,big=self.splitBST(root.left,V)
            root.left=big
            return [small,root]
