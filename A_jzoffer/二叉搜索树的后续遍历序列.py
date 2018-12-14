
首先是后序遍历，所以最后一个值是根节点，此时，由于是二叉搜索树，所以左子树的值都比右子树的值要小，我们找到
左右子树，然后判断一下右子树是不是都大于根节点（左子树不用判断因为在找左子树的时候已经判断了）
然后递归判断左子树和右子树满足不满足就好了


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) <= 0:
            return False
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        j = i
        for t in range(j,len(sequence)):
            if sequence[t] < root:
                return False
        left = True
        right = True
        if i > 0:left = self.VerifySquenceOfBST(sequence[:i])
        if j < len(sequence)-1:right = self.VerifySquenceOfBST(sequence[i:len(sequence)-1])
        
        return left and right