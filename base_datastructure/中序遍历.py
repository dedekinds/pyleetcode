# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return []
        if root:
            self.inorderTraversal(root.left)
            self.ans.append(root.val)
            self.inorderTraversal(root.right)
        return self.ans

_________________________________________________
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        if not root:return []
        
        def get_left(root,stack):
            stack.append(root)
            while root.left:
                stack.append(root.left)
                root = root.left
        get_left(root,stack)
        ans = []
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.right:
                get_left(temp.right,stack)
        return ans
                
                
                
                
                
        
