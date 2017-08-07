'''101. Symmetric Tree  
   2017.8.7
'''
用层次遍历，小心null的情况，实际上不需要像中间做法那样每次新建一个树
这是因为只要一旦有一个不对称就可以返回False了
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left),height(tree.right))+1

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        treeheight=height(root)
        Q=[root]
        hei=0
        while hei<=treeheight:
            hei+=1
            tempQ=[]
            templist=[]
            for x in Q:
                if x.left:
                    tempQ.append(x.left)
                    templist.append(x.left.val)
                elif x.left is None:
                    templist.append('a')#对比上一个方法改了这里
                    
                if x.right:
                    tempQ.append(x.right)
                    templist.append(x.right.val)
                elif x.right is None:
                    templist.append('a')
                    
            Q=tempQ
            if templist!=templist[::-1]:
                return False
        return True
                

 

————————————————————————
TLE
[9,14,14,74,null,null,74,null,12,12,null,63,null,null,63,-8,null,null,-8,-53,null,null,-53,null,-96,-96,null,-65,null,null,-65,98,null,null,98,50,null,null,50,null,91,91,null,41,-30,-30,41,null,86,null,-36,-36,null,86,null,-78,null,9,null,null,9,null,-78,47,null,48,-79,-79,48,null,47,-100,-86,null,47,null,67,67,null,47,null,-86,-100,-28,11,null,56,null,30,null,64,64,null,30,null,56,null,11,-28,43,54,null,-50,44,-58,63,null,null,-43,-43,null,null,63,-58,44,-50,null,54,43]
计算高度，对null的也补充进去了：181 / 193 test cases passed.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left),height(tree.right))+1

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        treeheight=height(root)
        Q=[root]
        hei=0
        while hei<=treeheight:
            hei+=1
            tempQ=[]
            templist=[]
            for x in Q:
                if x.left:
                    tempQ.append(x.left)
                    templist.append(x.left.val)
                elif x.left is None:
                    x.left=TreeNode('a')
                    tempQ.append(x.left)
                    templist.append(x.left.val)
                    
                if x.right:
                    tempQ.append(x.right)
                    templist.append(x.right.val)
                elif x.right is None:
                    x.right=TreeNode('a')
                    tempQ.append(x.right)
                    templist.append(x.right.val)
                    
            Q=tempQ
            if templist!=templist[::-1]:
                return False
        return True
                

————————————————————————————
WA：
第一个思路是直接考虑每一层，如果每一层的数组是对称的那么就OK
没考虑到null的情况，比如[1,3,3,null,4,null,4]