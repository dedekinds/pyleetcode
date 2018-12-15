顺序遍历并递归判断子树（感觉有点烧时间的方法

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def check(self,pRoot1,pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False#此时proot2不是none
        if pRoot1.val != pRoot2.val:
            return False
        return self.check(pRoot1.left,pRoot2.left) and self.check(pRoot1.right,pRoot2.right)
        
        
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        result = False
        if pRoot1.val == pRoot2.val:
            result = self.check(pRoot1,pRoot2)
        if not result:
            result =  self.HasSubtree(pRoot1.left,pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right,pRoot2)
        return result
        