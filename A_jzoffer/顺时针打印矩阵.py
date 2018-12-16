

有趣的思路
# -*- coding:utf-8 -*-
class Solution:
            
    def printMatrix(self, matrix):
        # write code here161
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for rows in matrix:
                    res.append(rows.pop())
            if matrix and matrix[0]:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for rows in matrix[::-1]:
                    res.append(rows.pop(0))
        return res


——————————————————
另一种神奇的方法
 可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如 
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可。

# -*- coding:utf-8 -*-
class Solution:
            
    def span(self,matrix):
        rows = len(matrix)
        col = len(matrix[0])
        ans = []
        for i in range(col):
            temp_ans = []
            for j in range(rows):
                temp_ans.append(matrix[j][i])
            ans.append(temp_ans)
        ans.reverse()
        return ans
        
    def printMatrix(self, matrix):
        # write code here161
        res = []
        while matrix:
            res += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.span(matrix)
        return res