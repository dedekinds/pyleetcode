'''109. Convert Sorted List to Binary Search Tree 
   2017.8.20
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#先用双指针来找到链表的中点，然后递归每一部分，取中点为新的结点，
#所得的树即为平衡二叉树（BST）

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:#处理长度为0的情况
            return None
        
        if head.next is None:#处理长度为1的情况
            return TreeNode(head.val)

        if head.next.next is None:#处理长度为2的情况
            temp=TreeNode(head.val)
            temp.right=TreeNode(head.next.val)
            return temp
        
        mid,temp=self.getmidpointer(head)
        root=TreeNode(mid.val)

        lhead=head
        rhead=mid.next
        temp.next=None
        #本来想让mid=None，但是实际上mid指向self.getmidpointer(head)，改变mid
        #是不会改变本来的指针的，不过如果是前一个指针temp的话，我们就可以用temp.next
        #来改变原来的指针的指向（区别可以参考148_Sort List_easy）
        
        root.left=self.sortedListToBST(lhead)
        root.right=self.sortedListToBST(rhead)    

        return root


    def getmidpointer(self,head):#用开满指针，由追及问题的解知道mid在中间
        #返回中点和中点的前一个指针

        if head is None:
            return head
        fast=head
        slow=head
        slowslow=head
        while fast.next and fast.next.next:
            slowslow=slow
            slow=slow.next
            fast=fast.next.next
        return slow,slowslow