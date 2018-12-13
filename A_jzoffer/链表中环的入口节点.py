
先快慢指针得到一个交点，这说明成环了
再在这个地方和初始的位置，都放快指针，这样相遇的地方就是环的起始位置

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:return pHead
        
        fast = pHead
        slow = pHead
        check = False
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                check = True
                break
        if not check:
            return None
        while fast != pHead:
            fast = fast.next.next
            pHead = pHead.next.next
        return pHead
        