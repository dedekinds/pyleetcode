
和从上往下打印二叉树那题一样的思路
用current和next两个来保存当前层还没打印的数和下一层要打印的数量
用两个栈就可以了
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:return []
        s1 = [pRoot]
        s2 = []
        flag = True
        current_num = 0
        next_num = 1
        res = []
        temp_res = []
        
        while s1 or s2:
            while next_num:
                
                if flag:
                    temp = s1.pop()
                    next_num -= 1
                    temp_res.append(temp.val)
                    if temp.left:
                        s2.append(temp.left)
                        current_num += 1
                    if temp.right:
                        s2.append(temp.right)
                        current_num += 1
                        
                if not flag:
                    temp = s2.pop()
                    next_num -= 1
                    temp_res.append(temp.val)
                    if temp.right:
                        s1.append(temp.right)
                        current_num += 1
                    if temp.left:
                        s1.append(temp.left)
                        current_num += 1
            flag = not flag
            res.append(temp_res)
            temp_res = []
            next_num = current_num
            current_num = 0
        return res
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        