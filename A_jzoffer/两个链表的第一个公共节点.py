'''
第一种方法是分别遍历出两个链表的长度num1和num2，然后让长的那个先走abs(num1 - num2)，然后再一起
出发，然后就可以遍历到公共节点了
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None 
        pt1 = pHead1
        pt2 = pHead2
        num1 = 0
        num2 = 0
        while pt1:
            num1 += 1
            pt1 = pt1.next
        while pt2:
            num2 += 1
            pt2 = pt2.next
            
        if num1 > num2:
            diff = num1 - num2
            while diff:
                pHead1 = pHead1.next
                diff -= 1
        else:
            diff = num2 - num1
            while diff:
                pHead2 = pHead2.next
                diff -= 1
                
        while pHead1:
            if pHead1 == pHead2:return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return None
            