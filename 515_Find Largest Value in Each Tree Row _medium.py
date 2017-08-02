'''515. Find Largest Value in Each Tree Row  
   2017.8.2
'''
用层次遍历框架即可
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        ans=[]
        if not root:
            return ans
        Q=[root]
        while Q:
            temp=Q[0].val
            tempQ=[]
            for x in Q:
                if x.val>=temp:
                    temp=x.val
                if x.left:tempQ.append(x.left)
                if x.right:tempQ.append(x.right)
            ans.append(temp)
            Q=tempQ
        return ans
                
        
        
