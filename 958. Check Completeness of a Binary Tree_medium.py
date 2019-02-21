# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
判断是否是完全二叉树，用层次遍历
一旦有null的时候停止下来，然后如果队列里面还有的话说明会出现左边是null右边有值的情况，返回false
否则是OK的
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        tree = [root]
        while tree[0]:
            temp = tree.pop(0)
            tree.append(temp.left)
            tree.append(temp.right)
        for node in tree:
            if node:
                return False
        return True
            