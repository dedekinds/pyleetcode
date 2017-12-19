
'''
234. Palindrome Linked List
2017.12.19
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
判断回文数，首先用，快慢指针来找到中点，然后反转后面的链表(这一步可以有O(1)空间的做法)
然后逐个判断！
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        #找到中点
        slow=head
        fast=head
        while fast.next and fast.next.next:#按fast.next fast.next.next的顺序写，另外如果fast.next不存在的话，不能有fast.next.next
            slow=slow.next
            fast=fast.next.next
        
        new=ListNode(0)
        s=slow.next
        while s:
            temp=s.next
            s.next=new.next
            new.next=s
            s=temp
        p=head
        q=new.next
        while q:
            if p.val!=q.val:
                return False
            p=p.next
            q=q.next
        return True
        
        if head.val==head.next.val:#剩下二元的情况
            return True
        else:
            return False

            
