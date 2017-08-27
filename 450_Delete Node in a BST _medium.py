'''450. Delete Node in a BST 
   2017.8.27
'''
邓俊辉30240184_07-B-8 删除-框架的思路
具体见笔记
单分支
双分支转换为单分支情况
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def search_BST(root,key):
    #查找函数，如果没找到就返回(-1,-1,-1)，如果找到就返回其
    #right:(父节点,本节点，1）
    #left:(父节点,本节点，0）
    if root is None:
        return -1,-1,-1
    if root.right:
        if root.right.val==key:
            return root,root.right,1
    if root.left:
        if root.left.val==key:
            return root,root.left,0
        
    if root.val<=key:
        return search_BST(root.right,key)
    else:
        return search_BST(root.left,key)


    
class Solution(object):
    
    #双分支
    def double_delete(self,tree):
        ans=tree
        ans_father=tree#寻找后继（即直接找删去目标的右结点的左极点）
        if tree.right:
            ans=tree.right
            lr=1
            while True:
                if ans.left is None:
                    break
                ans_father=ans
                ans=ans.left
                lr=0
        a=tree.val
        tree.val=ans.val
        ans.val=a
        
        check=0
        if ans.right:
            check+=1
        if ans.left:
            check+=1
        
        if check==0:#没有分支
            if lr==1:
                ans_father.right=ans.right#反正是空树
            if lr==0:
                ans_father.left=ans.right
            
        if check==1:#单分支
            self.single_delete(ans_father,ans,lr)

    
    #单分支：
    def single_delete(self,tree_father,tree,lr):
        if lr==1:
            if tree.right:
                tree_father.right=tree.right
            if tree.left:
                tree_father.right=tree.left
        if lr==0:
            if tree.right:
                tree_father.left=tree.right
            if tree.left:
                tree_father.left=tree.left

    #主程序   
    def deleteNode(self, root, key):
        if root is None:
            return root
        #处理删除的点恰好是顶点的情况（增加一个顶点[其中这个顶点我们选取为全局的最小值]）
        if root.val==key:
            
            minvalue=root.val
            pointer=root
            while True:
                if pointer.left is None:
                    break
                pointer=pointer.left
                minvalue=pointer.val
            new=TreeNode(minvalue-1)
            new.right=root
            return (self.deleteNode(new, key)).right
            
    
        #一般情况
        tree_father,tree,lr=search_BST(root,key)
        if lr==-1:
            return root
        #用check判断是单分支还是双分支
        check=0
        if tree.right:
            check+=1
        if tree.left:
            check+=1
        
        if check==0:#没有分支
            if lr==1:
                tree_father.right=tree.right#反正是空树
            if lr==0:
                tree_father.left=tree.right
            return root
        
        if check==1:#单分支
            self.single_delete(tree_father,tree,lr)
            return root
        
        if check==2:#双分支转换为单分支
            self.double_delete(tree)
            return root
        
        



_____________best code_______________________________
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                tmp = root.right
                root = None
                return tmp
            elif not root.right:
                tmp = root.left
                root = None
                return tmp
            tmp = self.treeMin(root.right)
            root.val = tmp.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root

    def treeMin(self, root):
        while root.left:
            root = root.left
        return root