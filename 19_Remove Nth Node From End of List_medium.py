'''
19. Remove Nth Node From End of List
2018.3.26
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        (1)首先在head前加多一个节点
        (2)构造快慢指针使得指针的间隔是n，这样的话大家都以1为步长前进的时候，一旦fast到达None的话，slow也到了处理的位置了
        (3)注意fast的初始化可能会越界，要特别判断，看**
        """
        temp = ListNode(0)
        temp.next = head
        
        slow = temp
        fast = temp
        for i in range(n+1):
            if fast:
                fast = fast.next
            else:
                for j in range(i-n):#** i此时就是长度
                    slow = slow.next
                    
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next=slow.next.next
        return temp.next