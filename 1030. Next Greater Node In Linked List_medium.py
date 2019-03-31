# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
单调栈模板
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        val = []
        while head:
            val.append(head.val)
            head = head.next
        stack = []
        res = [-1]*len(val)
        i = 0
        while i<len(val):
            if not stack or val[stack[-1]] >= val[i]:
                stack.append(i)
                i += 1
            else:
                res[stack[-1]] = val[i]
                stack.pop()

        while stack:
            res[stack[-1]] = 0
            stack.pop()
        return(res)
            
