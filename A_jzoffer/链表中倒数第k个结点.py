# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
双指针，让其中一个指针先走k-1步，注意k可能小于0或者大于链表的长度
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k <=0 or head is None:
            return None
        pt1 = head
        pt2 = head
        num = k-1
        while num and pt2.next:
            pt2 = pt2.next
            num -= 1
        if num > 0:
            return None#k可能比链表本身还长
        
        while pt2.next:
            pt2 = pt2.next
            pt1 = pt1.next
        return pt1