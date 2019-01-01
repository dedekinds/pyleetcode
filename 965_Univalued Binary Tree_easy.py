# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:return True
        check = root.val
        stack = [root]
        while stack:
            temp = stack.pop()
            if check != temp.val:return False
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        return True