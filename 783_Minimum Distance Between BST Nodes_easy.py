'''
783. Minimum Distance Between BST Nodes
2018.2.11
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #左节点的右极节点，或者右节点的左极节点
    def findmin(self,root):
        ans_left=0xfffffff
        ans_right=0xfffffff
        if root.left:
            ans_left=root.left.val
            temp=root.left.right
            while temp:
                ans_left=temp.val
                temp=temp.right
        if root.right:
            ans_right=root.right.val
            temp=root.right.left
            while temp:
                ans_right=temp.val
                temp=temp.left
        return min(abs(root.val-ans_left),abs(root.val-ans_right))
            
        
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.temp=0xfffffff
        def travel(root):
            if not root:
                return
            
            check=self.findmin(root)
            if check<self.temp:
                self.temp=check
            travel(root.right)
            travel(root.left)
        travel(root)
        return self.temp