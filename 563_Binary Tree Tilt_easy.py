'''
563. Binary Tree Tilt 
2017.11.16
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0#得到一个全局的变量
        def travel(root):#计算子树的val的和
            if root is None:
                return 0
            rootleft=travel(root.left)
            rootright=travel(root.right)
            self.ans+=abs(rootleft-rootright)#顺便把差计算出来
            return root.val+rootleft+rootright
            
        travel(root)
        return self.ans