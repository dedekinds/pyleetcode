"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:return 0
        temp_res = [self.maxDepth(tree) for tree in root.children]
        if temp_res:return max(temp_res)+1
        else:return 1
        