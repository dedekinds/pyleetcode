# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:return None
        if len(preorder) ==1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        flag = False
        for i in range(1,len(preorder)):
            if preorder[i]>preorder[0]:
                flag = True
                break
        if flag:
            left = self.bstFromPreorder(preorder[1:i])
            right = self.bstFromPreorder(preorder[i:])
            root.left = left
            root.right = right
            return root
        else:
            left = self.bstFromPreorder(preorder[1:])
            root.left = left
            root.right = None
            return root