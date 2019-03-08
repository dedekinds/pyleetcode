# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return []
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1:
            temp = stack1.pop()
            stack2.append(temp)
            if temp.left:stack1.append(temp.left)
            if temp.right:stack1.append(temp.right)
        ans = []
        while stack2:
            ans.append(stack2.pop().val)
        return ans
_______________________________________________________
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:return []
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.ans.append(root.val)
        return self.ans