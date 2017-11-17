'''
530. Minimum Absolute Difference in BST 
2017.11.17
'''
极小差必定是出现在root和它的左结点的极右结点或者右结点的极左结点的差上
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans=0x7FFFFFFF
        left=root.left
        right=root.right
        if left:
            while left.right:
                left=left.right#寻找左结点的极右结点
            ans=min(root.val-left.val,self.getMinimumDifference(root.left))
        if right:
            while right.left:
                right=right.left#寻找右结点的极左结点
            ans=min(ans,right.val-root.val,self.getMinimumDifference(root.right))
        return ans
