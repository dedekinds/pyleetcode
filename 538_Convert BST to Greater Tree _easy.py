'''
538. Convert BST to Greater Tree 
2017.11.12
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

右-中-左的中序遍历，题目意思实际上是说，对于BST某个结点
讲这个结点右边位置的所有值累加到自己身上
              5
            /   \
           2     13


                 18(5+13)
              /            \
          20(2+5+13)     13(13+0)


class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total=0#全局变量
        def travaltree(root):
            if root is None:
                return None
            travaltree(root.right)
            root.val+=self.total
            self.total=root.val
            travaltree(root.left)
        travaltree(root)
        return root
