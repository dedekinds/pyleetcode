# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, tree):
        # write code here
        ans = []
        if not tree:
            return ans
        q=Queue.Queue()
        q.put(tree)
        while not q.empty():
            tree = q.get()
            ans.append(tree.val)
            if tree.left:
                q.put(tree.left)
            if tree.right:
                q.put(tree.right)
        return ans
            
        