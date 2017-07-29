'''226. Invert Binary Tree 
   2017.7.29

'''
用层次遍历（好像层次用上瘾==、 超慢，好像超越了0.14%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        Q=[root]
        while Q:
            tempQ=[]
            for x in Q:
                temp=x.left
                x.left=x.right
                x.right=temp
                if x.left:
                    tempQ.append(x.left)
                if x.right:
                    tempQ.append(x.right)
            Q=tempQ
        return root

        


——————————best code—————————————

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root!=None:
        	root.right, root.left = root.left, root.right
            root.right=self.invertTree(root.right)
            root.left=self.invertTree(root.left)
        return root