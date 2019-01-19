# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        fast = head
        slow = head
        tmp = res
        if not fast or not fast.next:
            return head

        
        while fast and fast.next:
            fast = fast.next.next
            tmp.next = slow.next
            tmp.next.next = slow
            tmp = tmp.next.next
            if not fast:
                tmp.next = None#偶数,没有置none的话会有bug
            elif not fast.next:
                tmp.next = fast#奇数
            slow = fast
            
        return res.next
