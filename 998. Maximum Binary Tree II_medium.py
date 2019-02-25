有点暴力了，还原了list再构造树（之前的题目
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def get_A(self,root):
        if not root.left and not root.right:
            return [root.val]
        if not root.right:
            return self.get_A(root.left) + [root.val]
        if not root.left:
            return [root.val] + self.get_A(root.right) 
        else:
            return self.get_A(root.left) + [root.val] + self.get_A(root.right)
        
    def get_tree(self,nums):
        if not nums:
            return None
        max_val = max(nums)
        root = TreeNode(max_val)
        max_index = nums.index(max_val)
        root.left = self.get_tree(nums[:max_index])
        root.right = self.get_tree(nums[(max_index+1):])
        return root
        
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        nums = self.get_A(root)
        nums.append(val)
        return self.get_tree(nums)
        
        
            
        