
'''104. Maximum Depth of Binary Tree 
   2017.7.29
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def height(tree):
    if not tree:
        return 0
    return max(height(tree.left),height(tree.right))+1
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return height(root)
        