地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

# -*- coding:utf-8 -*-
class Solution:
    def counting(self,num):
        s = 0
        temp = str(num)
        for i in range(len(temp)):
            s += int(temp[i])
        return s
 
    def movingCount(self,threshold, rows, cols):
        # write code here
        if threshold < 0:return 0
        stack = [(0,0)]
        cnt = 0
        visited = [[0]*cols for i in range(rows)]
        visited[0][0] = 1
        while stack:
            cnt += 1
            temp = stack.pop()
            i = temp[0]
            j = temp[1]
            if i-1 >=0 and self.counting(i-1)+self.counting(j) <= threshold and visited[i-1][j] == 0:
                stack.append((i-1,j))
                visited[i-1][j] = 1
            if i+1 < rows and self.counting(i+1)+self.counting(j) <= threshold and visited[i+1][j] == 0:
                stack.append((i+1,j))
                visited[i+1][j] = 1
            if j-1 >=0 and self.counting(i)+self.counting(j-1) <= threshold and visited[i][j-1] == 0:
                stack.append((i,j-1))
                visited[i][j-1] = 1
            if j+1 < cols and self.counting(i)+self.counting(j+1) <= threshold and visited[i][j+1] == 0:
                stack.append((i,j+1))
                visited[i][j+1] = 1
        return cnt