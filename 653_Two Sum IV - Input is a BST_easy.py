'''653. Two Sum IV - Input is a BST  
   2017.9.11
'''
中序遍历+跌跤的2point大法可以AC
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twopoint(self,nums,k):
        if len(nums)==1:
            return False
        left=0
        right=len(nums)-1
        while left<right:
            Sum=nums[left]+nums[right]
            if Sum<k:
                left+=1
            elif Sum>k:
                right-=1
            else:
                return True
        return False
        
    def goAlongLeftBranch(self,tree,s):
        while tree:
            s.append(tree)
            tree=tree.left
    def findTarget(self, root, k):
        s=[]
        ans=[]
        while True:
            self.goAlongLeftBranch(root,s)
            if len(s)==0:
                break
            root=s.pop()
            ans.append(root.val)
            root=root.right
        return self.twopoint(ans,k)
        #return ans


        _________________________________
        best code
队列+集合 很好很好
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def findTarget(self, root, k):
        q = deque([root])
        v = set()
        while q:
            c = q.popleft()
            if k - c.val in v:
                return True
            v.add(c.val)
            if c.left:
                q.append(c.left)  
            if c.right:
                q.append(c.right)

        return False