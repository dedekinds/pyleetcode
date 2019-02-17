# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        Q = [root]
        valueQ = [root.val]
        pretemp = [root]
        depth = 1
        while Q:
            tempQ = []
            tempvalueQ = []
            
            for a in Q:
                if a.left:
                    tempQ.append(a.left)
                    tempvalueQ.append(a.left.val)
                if a.right:
                    tempQ.append(a.right)
                    tempvalueQ.append(a.right.val)
            depth += 1
            #print(pretemp)
            pretemp = Q
            if x in tempvalueQ and y in tempvalueQ:
                #print(pretemp)
                #print(depth)
                for tmp in pretemp:
                    if tmp.left and tmp.right:
                        #print(tmp.left.val,tmp.right.val,tmp.val)
                        if tmp.left.val in [x,y] and tmp.right.val in [x,y]:
                            return False
                return True
            Q = tempQ
            valueQ = tempvalueQ
        return False