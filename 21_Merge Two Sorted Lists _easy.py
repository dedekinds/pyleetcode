'''
21. Merge Two Sorted Lists 
2017.12.11
'''

逐个对比O(m+n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None or l2 is None:
            return [l1,l2][l1 is None]
        
        temp=ListNode(-1)
        pointer=temp
        p=l1
        q=l2
        while q and p:
            pointer.next=[p,q][q.val<=p.val]
            pointer=pointer.next
            if q.val<=p.val:
                q=q.next
            else:
                p=p.next

        pointer.next=[p,q][p is None]
        return temp.next
            
        
