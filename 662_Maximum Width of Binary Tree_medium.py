'''662. Maximum Width of Binary Tree 
   2017.9.13
'''
基于一个这样的编码：
         1
        2  3
       4 5 6 7
      8 9 ...
即：
        c
      2c  2c+1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0
        Q=[root]
        root.val=1
        width=1
        while Q:
            tempQ=[]
            check=[]
            for x in Q:
                if x.left:
                    x.left.val=x.val*2
                    tempQ.append(x.left)
                    check.append(x.left.val)
                if x.right:
                    x.right.val=x.val*2+1
                    tempQ.append(x.right)
                    check.append(x.right.val)
            if len(check)==0:
                break
            if width<=(check[-1]-check[0]+1):
                width=check[-1]-check[0]+1
            Q=tempQ
        return width
        
——————————————————————————————————————————————————————————
一个暴力的思路，首先计算深度，然后构造一个O(n)的双指针函数计算每一层的宽度
最后套入层次遍历当中，但是TLE：104/108，悲剧
def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left),height(tree.right))+1

class Solution(object):
    def search(self,nums):
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left]!='dede' and nums[right]!='dede':
                return right-left+1
            elif nums[left]!='dede':
                right-=1
                continue
            else:
                left+=1
                continue
        return -1
                
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0
        hei=height(root)
        Q=[root]
        length=1
        h=1
        while h<=hei:
            h+=1
            tempQ=[]
            truetemp=[]
            for x in Q:
                if x.left:
                    tempQ.append(x.left)
                    truetemp.append(x.left.val)
                if not x.left:
                    x.left=TreeNode('dede')
                    tempQ.append(x.left)
                    truetemp.append(x.left.val)
                if x.right:
                    tempQ.append(x.right)
                    truetemp.append(x.right.val)
                if not x.right:
                    x.right=TreeNode('dede')
                    tempQ.append(x.right)
                    truetemp.append(x.right.val)
            a=self.search(truetemp)
            #print(a)
            if a>=length:
                length=a
            Q=tempQ
        return length

