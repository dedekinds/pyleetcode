# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return []
        ans = []
        stack = [root]
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.right:stack.append(temp.right)
            if temp.left:stack.append(temp.left)
        return ans
