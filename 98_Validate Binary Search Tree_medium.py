# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


直接用中序遍历然后从左到右计算
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans = []
        def inorder(root):
            if not root:return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        #if root.left:
        inorder(root)
        for i in range(len(ans)-1):
            if ans[i] >= ans[i+1]:
                return False
        return True
——————————————————————————————————————————————————————————
BST三种特性
除了自身要和左右孩子的顶点比较之外，还要保证当前节点是左子树的最大值，是右子树的最小值
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
        def helper(root,maxv,minv):
            if not root:return True
            if root.val <= minv or root.val >= maxv:return False
            if root.left and root.val <= root.left.val:return False
            if root.right and root.val >= root.right.val:return False
            return helper(root.left,root.val,minv) and helper(root.right,maxv,root.val)
        return helper(root,float('inf'),-float('inf'))
        
        
        