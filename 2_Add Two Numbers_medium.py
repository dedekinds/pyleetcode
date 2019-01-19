# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
加一个数组来存每位计算的结果
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack = []
        while l1 and l2:
            stack.append(l1.val+l2.val)
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                stack.append(l1.val)
                l1 = l1.next
        if l2:
            while l2:
                stack.append(l2.val)
                l2 = l2.next
        res = ListNode(-1)
        ans = res
        print(stack)
        for i in range(len(stack)):
            if stack[i] >= 10:
                res.next = ListNode(stack[i]%10)
                if i < len(stack)-1:
                    stack[i+1] += 1
                if i >= len(stack)-1:
                    res.next.next = ListNode(1)
            else:
                res.next = ListNode(stack[i])
            res = res.next
                    
        return ans.next
        