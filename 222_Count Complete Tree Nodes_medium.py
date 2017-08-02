'''222. Count Complete Tree Nodes 
   2017.8.2
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0
        countl=0
        countr=0
        L=root
        R=root
        while L:
            countl+=1
            L=L.left
        while R:
            countr+=1#对比一下下面的方法的这里，科科，居然过了14/17
            R=R.right
        if countl==countr:
            return (1<<countr)-1#为什么1<<countr会出错？没打括号
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
 ——————————————————————————————————————————————————————————————————————           
        

计算数的最左结点和最右结点，如果高度相同，那么就是完全二叉树，
否则就返回1+递归(左子树)+递归(右子树)
TLE
class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0
        countl=0
        countr=0
        L=root
        R=root
        while L:
            countl+=1
            L=L.left
        while R:
            countr==1
            R=R.right
        if countl==countr:
            return pow(2,countl)-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
————————————————————————————
算高度，然后遍历最后一层，合算节点数TLE
def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left),height(tree.right))+1

class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0
        Q=[root]
        cen=1
        high=height(root)
        while cen<high:
            tempQ=[]
            cen+=1
            for x in Q:
                if x.left:
                    tempQ.append(x.left)
                if x.right:
                    tempQ.append(x.right)
            Q=tempQ
        return len(Q)+pow(2,high-1)-1
————————————————————————————————
裸层次遍历TLE：
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        Q=[root]
        ans=1
        while Q:
            tempQ=[]
            for x in Q:
                if x.left:
                    tempQ.append(x.left)
                    ans+=1
                if x.right:
                    tempQ.append(x.right)
                    ans+=1
            Q=tempQ
        return ans
            
        