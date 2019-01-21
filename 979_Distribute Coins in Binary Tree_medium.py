https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal
非常有趣的一个问题
注意审题，由于有N个coin和N个顶点，所以所有的coin除了保留给自己一个都要运输出去！
class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans += abs(left) + abs(right)
            
            return left + right + root.val -1
        dfs(root)
        return self.ans