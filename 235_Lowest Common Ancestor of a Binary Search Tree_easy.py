'''
235. Lowest Common Ancestor of a Binary Search Tree (LCA)
2017.12.10
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
由二叉搜索树的性质，可以观察到，最小公共祖先满足如下性质：
从最开始的结点出发，如果，root在p q之间或者直接等于p q中的一个，那么它就是最小公共祖先，如果
均大于p q那么左偏，如果均小于那么右偏
类似地迭代即可

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        while True:
            if root.val==p.val or root.val==q.val:
                return root
            elif root.val>p.val and root.val>q.val:
                root=root.left
                continue
            elif root.val<p.val and root.val<q.val:
                root=root.right
                continue
            else:
                return root#在 p q 之间


________________________________
简短的代码
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        while (p.val - root.val) * (q.val - root.val) > 0:
            root = [root.left, root.right][p.val > root.val]
        return root