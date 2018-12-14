
中序遍历，注意k的大小

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def get_left(self,root,stack):
        stack.append(root)
        while root.left:
            stack.append(root.left)
            root = root.left
            
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k<=0:return None
        stack = []
        res = []
        self.get_left(pRoot,stack)
        
        while stack:
            temp = stack.pop()
            res.append(temp)
            if temp.right:
                temp = temp.right
                self.get_left(temp,stack)
        if k > len(res):return None
        return res[k-1]
        