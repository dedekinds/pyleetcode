'''
83. Remove Duplicates from Sorted List
2017.12.6
'''
操作：用temp也指向这个链表，然后修改temp，最后返回head就可以了
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=head
        while temp and temp.next:
            if temp.val==temp.next.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
