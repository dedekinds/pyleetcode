有点暴力了，还原了list再构造树（之前的题目
import collections
class Solution(object):
    def get_A(self,root):
        if not root.left and not root.right:
            return [root.val]
        if not root.right:
            return self.get_A(root.left) + [root.val]
        if not root.left:
            return [root.val] + self.get_A(root.right) 
        else:
            return self.get_A(root.left) + [root.val] + self.get_A(root.right)
        
        
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        nums = self.get_A(root)
        nums.append(val)
        
        
        if not nums:
            return
        root = TreeNode(max(nums))
        max_idx = nums.index(max(nums))
        z, y = nums[:max_idx], nums[(max_idx+1):]
        self.dfs(root, z, left=1, right=0)
        self.dfs(root, y, left=0, right=1)
        return root
        
        
    def dfs(self, root, l, left, right):
        if not l:
            return
        max_v = max(l)
        max_idx = l.index(max_v)
        z, y = l[:max_idx], l[(max_idx+1):]
        if left:
            root.left = TreeNode(max_v)
            self.dfs(root.left, z, left=1, right=0)
            self.dfs(root.left, y, left=0, right=1)
        if right:
            root.right = TreeNode(max_v)
            self.dfs(root.right, z, left=1, right=0)
            self.dfs(root.right, y, left=0, right=1)
            
        