'''148. Sort List 
   2017.7.12

'''
http://blog.csdn.net/aliceyangxi1987/article/details/50724617
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        mid=self.getmidpointer(head)
        lhead=head
        rhead=mid.next
        mid.next=None#之前缺少这句一直RE，超出递归深度
        return self.merge(self.sortList(lhead),self.sortList(rhead))



    def getmidpointer(self,head):
        if head is None:
            return head
        fast=head
        slow=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    
    def merge(self,lhead,rhead):
        temp=ListNode(0)
        ans=temp#用ans来指向temp
        while lhead and rhead:
            if lhead.val<rhead.val:
                temp.next=lhead
                lhead=lhead.next
            else:
                temp.next=rhead
                rhead=rhead.next
            temp=temp.next
        if lhead:
            temp.next=lhead
        else:
            temp.next=rhead
        return ans.next

