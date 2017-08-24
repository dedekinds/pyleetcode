'''654. Maximum Binary Tree 
   2017.8.24
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):



        if not nums :#if nums is None:不行
            return None
        temp=max(nums)
        root=TreeNode(temp)
        location=nums.index(temp)
        root.left=self.constructMaximumBinaryTree(nums[:location])
        root.right=self.constructMaximumBinaryTree(nums[(location+1):])
        
        return root
        """
        a=[]
        if nums is None:
            return 1
        else:
            return 2
        
        结果为2，对于[],不算None哦
        '''
        