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