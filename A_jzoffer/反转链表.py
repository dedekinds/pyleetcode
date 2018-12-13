pre一开始指向None
curr 为当前
NEX 为下一个
不断往前赋值即可



# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:return pHead
        pre = None#ListNode(-1)
        curr = pHead
        NEX = curr.next
        
        while NEX:
            curr.next = pre
            
            pre = curr
            curr = NEX
            NEX = curr.next
            
        curr.next = pre
        return curr