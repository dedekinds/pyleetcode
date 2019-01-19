# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
用优先队列的话可以做到O(Nlogk)
from Queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = ListNode(-1)
        tmp = res
        Q = PriorityQueue()
        for node in lists:
            if node:
                Q.put((node.val,node))
        while not Q.empty():
            val,node = Q.get()
            tmp.next = ListNode(val)
            tmp =tmp.next
            node = node.next
            if node:
                Q.put((node.val,node))
        
        return res.next

___________________________________
O(kN)的做法
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = ListNode(-1)
        tmp = res
        while True:
            minv = float('inf')
            minindex = -1
            stop = True
            
            for i in range(len(lists)):
                if lists[i]:
                    #print(lists[i].val)
                    stop = False
                    if lists[i].val <= minv:
                        minindex = i
                        minv = lists[i].val
            if stop:break
            minnode = lists[minindex]
            tmp.next = ListNode(minnode.val)
            tmp = tmp.next
            lists[minindex] = lists[minindex].next 
            #minnode =minnode.next会错误，从列表中弹出数和赋值出来是不一样的
               
            
        return res.next