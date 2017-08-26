'''102. Binary Tree Level Order Traversal 
   2017.8.26
'''
层次遍历裸题
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        Q=[root]
        ans=[[root.val]]
        while Q:
            tempQ=[]
            tempans=[]
            for x in Q:
                if x.left:
                    tempQ.append(x.left)
                    tempans.append(x.left.val)
                if x.right:
                    tempQ.append(x.right)
                    tempans.append(x.right.val)
            Q=tempQ
            ans.append(tempans)
        ans.pop()
        return ans