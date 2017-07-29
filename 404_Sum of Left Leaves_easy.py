'''404. Sum of Left Leaves 
   2017.7.29

'''
用层次遍历，不过最关键还是读懂题意，科科

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        ans=0
        Q=[root]
        while Q:
            tempQ=[]
            for x in Q:
                if x.left:
                    if not x.left.left and not x.left.right:
                        ans+=x.left.val
                    tempQ.append(x.left)
                if x.right:
                    tempQ.append(x.right)
            Q=tempQ
        return ans

            
        
        
