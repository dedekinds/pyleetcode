# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

遍历到叶节点如果值为0那么就OK
class Solution:
    def hasPathSum(self, root, Sum):
        if not root:return False
        stack = [(root,Sum - root.val)]
        while stack:
            tree, value = stack.pop()
            if not tree.right and not tree.left and value == 0:
                return True
            if tree.right:
                stack.append((tree.right,value - tree.right.val))
            if tree.left:
                stack.append((tree.left,value - tree.left.val))
        return False
        
————————————————————————————————————————————————————————————
class Solution: 
    def hasPathSum(self, root, Sum):
        if not root:return False
        Sum -= root.val
        if not root.left and not root.right and Sum == 0:
            return True
        return self.hasPathSum(root.left,Sum) or self.hasPathSum(root.right,Sum)
