

'''623. Add One Row to Tree 
   2017.9.5
'''

利用层次遍历，注意深度为1的情况
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d==1:
            ans=TreeNode(v)
            ans.left=root
            return ans
        cen=1
        Q=[root]
        while Q:
            tempQ=[]
            for x in Q:
                if x.left:
                    tempQ.append(x.left)
                if x.right:
                    tempQ.append(x.right)
            cen+=1
            if cen==d:
                break
            Q=tempQ

                
        for y in Q:
            if y.left:
                temp=y.left
                y.left=TreeNode(v)
                y.left.left=temp
            if not y.left:
                y.left=TreeNode(v)
            if y.right:
                temp=y.right
                y.right=TreeNode(v)
                y.right.right=temp
            if not y.right:
                y.right=TreeNode(v)
        return root
        
        
        