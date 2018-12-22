这题非常坑，注意所有节点的左孩子都要置None,且最后一个节点的左右孩子都要置None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def get_left_branch(self,root,s):
        while root:
            s.append(root)
            root = root.left

            
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:return root
        s = []
        news = TreeNode(-1)
        res = news
        res.left = None
        while True:
            self.get_left_branch(root,s)
            if len(s) == 0:
                break
            root = s.pop()
            
            news.right = root
            news.left = None
            news = news.right
            
            root = root.right
        news.left = None
        news.right = None
        return res.right
            

        