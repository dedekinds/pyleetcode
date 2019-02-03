# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
从叶子开始合并，一直到最上面
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root:''
        if not root.left and not root.right:
            return chr(root.val + 97)
        if root.right and not root.left:
            return self.smallestFromLeaf(root.right) + chr(root.val + 97)
        if root.left  and not root.right:
            return self.smallestFromLeaf(root.left) + chr(root.val + 97)
        if root.right and root.left:
            left = self.smallestFromLeaf(root.left)
            right = self.smallestFromLeaf(root.right)
            return [right,left][left < right] + chr(root.val + 97)
            
        
        