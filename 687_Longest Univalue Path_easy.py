'''
687. Longest Univalue Path
2018.1.24
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#感觉还是重复计算了

class Solution(object):
    def get_num_longest(self,root,val):#以当前节点为初始点的最长路径
        if not root or root.val !=val:
            return 0
        return 1+max(self.get_num_longest(root.left,val),self.get_num_longest(root.right,val))
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left=root.left
        right=root.right
        val=root.val
        return max( self.get_num_longest(left,val)+self.get_num_longest(right,val), self.longestUnivaluePath(left),self.longestUnivaluePath(right))
        
————————————————best code_________________
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        longpaths = []
        
        def getLongest(node, parent_val):
            if node is None: return 0
            if node.val == parent_val:
                return (max(getLongest(node.left, node.val), getLongest(node.right, node.val)) + 1)
            else:
                longpaths.append(getLongest(node.left, node.val) 
                                 + getLongest(node.right, node.val))
                return 0
        getLongest(root, None)
        return max(longpaths) if longpaths else 0