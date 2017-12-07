'''
437. Path Sum III 
2017.12.7
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#这个方法是T(n)=2T(n/2)+n的，即nlogn
#遍历整颗树，并在每一个结点处，寻找以这个结点为开始的path和为Sum的路径
#在find_path中如果每到root.val==Sum那么说明构成一条path

def find_path(root,Sum):
    if root:
        return int(root.val==Sum)+find_path(root.left,Sum-root.val)+find_path(root.right,Sum-root.val)#O(n)
    return 0

class Solution:
    def pathSum(self, root, Sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return find_path(root,Sum)+self.pathSum(root.right,Sum)+self.pathSum(root.left,Sum)
        return 0
        