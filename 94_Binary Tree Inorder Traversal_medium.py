'''94. Binary Tree Inorder Traversal 
   2017.9.9
'''
二叉树的中序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def goAlongLeftBranch(self,tree,s):
        while tree:
            s.append(tree)
            tree=tree.left
    def inorderTraversal(self, root):
        s=[]
        ans=[]
        while True:
            self.goAlongLeftBranch(root,s)
            if len(s)==0:
                break
            root=s.pop()
            ans.append(root.val)
            root=root.right
        return ans
