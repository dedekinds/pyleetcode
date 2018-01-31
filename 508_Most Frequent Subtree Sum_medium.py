'''
508. Most Frequent Subtree Sum
2018.1.31
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def subsum(self,root):
        if not root:
            return 0
        return root.val+self.subsum(root.left)+self.subsum(root.right)

        
    def findFrequentTreeSum(self, root):
        cnt = collections.Counter()#用cnt=dict()不可以，用counter的话自动初始化为0
        
        def traveltree(root):
            if not root:
                return 
            cnt[self.subsum(root)]+=1
            traveltree(root.right)
            traveltree(root.left)
            
        traveltree(root)
        maxtemp=max(cnt.values()+[None])
        
        return [e for e,v in cnt.iteritems() if v == maxtemp]
        