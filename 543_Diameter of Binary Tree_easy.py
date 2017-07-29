
'''543. Diameter of Binary Tree 
   2017.7.29

'''




——————错误的：直觉告诉我，最长路径必定会经过顶点，结果过了102/106，但实际上不是
反例：[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
def height(tree):
    if not tree:
        return 0
    return max(height(tree.left),height(tree.right))+1

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return height(root.right)+height(root.left)
