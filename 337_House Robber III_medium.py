'''
337. House Robber III
2018.3.8
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        每次返回两个值，分别表示偷或不偷该节点的最大收益
        """
        def solve(root):
            if not root:
                return [0,0]#第0位表示偷该节点，第1位表示不偷该节点
            left ,right=solve(root.left) ,solve(root.right)
            return [root.val+left[1]+right[1] , (max(left)+max(right))]
        
        return max(solve(root))
        