'''513. Find Bottom Left Tree Value 
   2017.8.16
'''
层次遍历
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
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Q=[root]
        heig=height(root)
        temp=0
        while temp<heig-1:
            temp+=1
            tempQ=[]
            for x in Q:
                if x.left:
                    tempQ.append(x.left)
                if x.right:
                    tempQ.append(x.right)
            Q=tempQ
        return Q[0].val
                
            
        