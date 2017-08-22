'''144. Binary Tree Preorder Traversal 
   2017.8.22
'''
二叉树的先序遍历
对比145. Binary Tree Postorder Traversal 
采用的是可扩展的办法，即不断遍历左子树，用栈存右子树
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

        
class Solution(object):
    
    def visitleft(self,tree,s,ans):
        while tree:
            ans.append(tree.val)
            if tree.right:
                s.append(tree.right)
            tree=tree.left
        
    def preorderTraversal(self, root):

        stack=[]
        ans=[]
        while True:
            self.visitleft(root,stack,ans)
            if len(stack)==0:
                break
            root=stack.pop()
            
        return ans
        
        
        
        
        

