'''230. Kth Smallest Element in a BST 
   2017.9.9
'''
因为是BST所以是有序的，可以强行中序遍历，O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def goAlongLeftBranch(self,tree,s):
        while tree:
            s.append(tree)
            tree=tree.left
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        s=[]
        ans=[]
        while True:
            self.goAlongLeftBranch(root,s)
            if len(s)==0:
                break
            root=s.pop()
            ans.append(root.val)
            root=root.right
        return ans[k-1]
