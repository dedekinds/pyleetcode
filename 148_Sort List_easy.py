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
        #用归并排序的办法(链表版)
        if head is None or head.next is None:
            return head
        mid=self.getmidpointer(head)
        lhead=head
        rhead=mid.next
        mid.next=None#之前缺少这句一直RE，超出递归深度?
        #因为如果没有这句的话，lhead=head在到达mid的时候还会继续下去，
        #以[2,2,1,5,6]为例，要使得在merge中ok，且head~=[2,2,1]的话必须在
        #mid.next赋值忘后设为None
        return self.merge(self.sortList(lhead),self.sortList(rhead))



    def getmidpointer(self,head):#用开满指针，由追及问题的解知道mid在中间
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

