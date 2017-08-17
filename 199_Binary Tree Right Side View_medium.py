'''199. Binary Tree Right Side View 
   2017.8.17
'''
层次遍历的裸题
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        ans=[root.val]
        Q=[root]
        while Q:
            tempQ=[]
            for x in Q:
                if x.left:
                    tempQ.append(x.left)
                if x.right:
                    tempQ.append(x.right)
            if len(tempQ)>0:
                ans.append(tempQ[-1].val)
            Q=tempQ
        return ans
