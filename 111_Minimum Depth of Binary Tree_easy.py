
'''111. Minimum Depth of Binary Tree 
   2017.7.29

'''
层次遍历（BFS

def height(tree):
    if not tree:
        return 0
    return max(height(tree.left),height(tree.right))+1
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        Q=[root]
        ans=pow(2,31)
        cen=0#表示到达的层数
        while Q:
            cen+=1
            tempQ=[]
            for tree in Q:
                if not tree.left and not tree.right:#如果某个端点没有后续，那么就记录它此时的层数
                    ans=min(ans,cen)
                if tree.left:
                    tempQ.append(tree.left)
                if tree.right:
                    tempQ.append(tree.right)
            Q=tempQ
        return ans
                    