'''145. Binary Tree Postorder Traversal 
   2017.8.22
'''
对比144. Binary Tree Preorder Traversal 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def visitright(self,tree,s,ans):
        while tree:
            ans.insert(0,tree.val)
            if tree.left:
                s.append(tree.left)
            tree=tree.right
            
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        ans=[]
        while True:
            self.visitright(root,stack,ans)
            if len(stack)==0:
                break
            root=stack.pop()
            
        return ans 
