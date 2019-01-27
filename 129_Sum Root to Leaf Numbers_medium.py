# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self,root,presum):
        if not root:return 0
        if not root.left and not root.right:
            return 10*presum + root.val
        if root.left and root.right:
            left = self.dfs(root.left,10*presum + root.val)
            right = self.dfs(root.right,10*presum + root.val)
            return left + right
        #否则那么就是只有一个边
        if root.left:
            return self.dfs(root.left,10*presum + root.val)
        if root.right:
            return self.dfs(root.right,10*presum + root.val)
        
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        presum = 0
        return self.dfs(root,presum)
