'''107. Binary Tree Level Order Traversal II 
   2017.8.7
'''
层次遍历裸题
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        Q=[root]
        ans=[]
        while Q:
            tempQ=[]
            tempval=[]
            for x in Q:
                if x.left:
                    tempQ.append(x.left)
                    tempval.append(x.left.val)
                if x.right:
                    tempQ.append(x.right)
                    tempval.append(x.right.val)
            Q=tempQ
            ans.insert(0,tempval)
        ans.append([root.val])
        ans.pop(0)
        return ans
        