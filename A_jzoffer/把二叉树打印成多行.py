用一个current_num 和 next_num来表示剩余多少个数要输出已经下一轮要输出多少个数
用队列来层次遍历

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here173
        if not pRoot:return []
        Q = Queue.Queue()
        Q.put(pRoot)
        
        res = []
        temp_res = []
        current_num = 0
        next_num = 1
        while not Q.empty():
            while next_num:
                temp = Q.get()
                temp_res.append(temp.val)
                next_num -= 1
                if temp.left:
                    Q.put(temp.left)
                    current_num += 1
                if temp.right:
                    Q.put(temp.right)
                    current_num += 1
            res.append(temp_res)
            temp_res = []
            next_num = current_num 
            current_num = 0
        return res
            
        