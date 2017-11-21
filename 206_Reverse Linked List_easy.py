'''
206. Reverse Linked List 
2017.11.21
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new=ListNode(0)
        while head:
            temp=head.next
            head.next=new.next
            new.next=head
            head=temp
        return new.next
