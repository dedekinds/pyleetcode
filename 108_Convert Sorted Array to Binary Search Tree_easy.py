'''108. Convert Sorted Array to Binary Search Tree 
   2017.8.20
'''
和109. Convert Sorted List to Binary Search Tree 类似，用
中值+递归即可
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        if len(nums)==2:
            temp=TreeNode(nums[0])
            temp.right=TreeNode(nums[1])
            return temp
        
        length=len(nums)
        root=TreeNode(nums[int(length/2)])
        root.left=self.sortedArrayToBST(nums[:(int(length/2))])
        root.right=self.sortedArrayToBST(nums[(int(length/2)+1):])
        
        return root
        

