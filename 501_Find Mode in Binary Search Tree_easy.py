
'''
501. Find Mode in Binary Search Tree
2017.12.19
'''
暴力遍历树，然后用字典来存，最后找到最大值，以及它的位置
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        temp={}
        def travel(root):
            if root is None:
                return
            if root.val in temp:
                temp[root.val]+=1
            else:
                temp[root.val]=1
            travel(root.left)
            travel(root.right)
        travel(root)
        
        tempmax=max(temp.values())
        return [x for x,y in temp.iteritems() if y == tempmax]
