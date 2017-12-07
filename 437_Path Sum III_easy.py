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
        


________________
Two Sum Method: Optimized Solution  O(N)

    A more efficient implementation uses the Two Sum idea. It uses a hash table (extra memory of order N). With more space, it gives us an O(N) complexity.
    As we traverse down the tree, at an arbitrary node N, we store the sum until this node N (sum_so_far (prefix) + N.val). in hash-table. Note this sum is the sum from root to N.
    Now at a grand-child of N, say G, we can compute the sum from the root until G since we have the prefix_sum until this grandchild available.We pass in our recursive routine.
    How do we know if we have a path of target sum which ends at this grand-child G? Say there are multiple such paths that end at G and say they start at A, B, C where A,B,C are predecessors of G. Then sum(root->G) - sum(root->A) = target. Similarly sum(root->G)-sum(root>B) = target. Therefore we can compute the complement at G as sum_so_far+G.val-target and look up the hash-table for the number of paths which had this sum
    Now after we are done with a node and all its grandchildren, we remove it from the hash-table. This makes sure that the number of complement paths returned always correspond to paths that ended at a predecessor node.

class Solution(object):
    def helper(self, root, target, so_far, cache):
        if root:
            complement = so_far + root.val - target
            if complement in cache:
                self.result += cache[complement]
            cache.setdefault(so_far+root.val, 0)
            cache[so_far+root.val] += 1
            self.helper(root.left, target, so_far+root.val, cache)
            self.helper(root.right, target, so_far+root.val, cache)
            cache[so_far+root.val] -= 1
        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result
