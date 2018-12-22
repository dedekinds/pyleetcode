"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        Q = []
        Q.append(root)
        
        res = []
        temp_res = []
        curr = 0
        next_num = 1
        
        while Q:
            while next_num:
                temp = Q.pop(0)
                temp_res.append(temp.val)
                next_num -= 1
                for i in temp.children:
                    Q.append(i)
                    curr += 1
            res.append(temp_res)
            temp_res = []
            next_num = curr
            curr = 0
        return res
        