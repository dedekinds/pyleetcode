'''
671. Second Minimum Node In a Binary Tree 
2017.11.30
'''
树很有特点，就是该节点上的值等于两个节点中较小的值
这么一来，根节点的值就是全局最小值了，所以只需要遍历寻找全局次小值即可
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minroot=root.val
        self.ans=0x80000000
        def traval(root):
            if root is None:
                return root
            if root.val>minroot and root.val<self.ans:
                self.ans=root.val
            traval(root.left)
            traval(root.right)
        traval(root)
        
        if self.ans==0x80000000:
            return -1
        else:
            return self.ans
