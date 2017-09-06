'''203. Remove Linked List Elements 
   2017.9.6
'''
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp=ListNode(0)
        temp.next=head#建立一条新链
        
        pre=temp#设定指针
        now=head
        while now:
            if now.val==val:
                pre.next=now.next
                now=now.next
            else:
                pre=now
                now=now.next
        return temp.next
