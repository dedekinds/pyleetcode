'''
695. Max Area of Island 
2017.11.9
'''
用了一个DFS，用一个栈来实现，每次搜索四个合法方向是否为1 ，是的话就入栈
且自身变为0

def legal_location(i,j,m,n):
    if i>-1 and i<n and j>-1 and j<m:#判断边界
        return True
    else:
        return False
class Solution:
    def maxAreaOfIsland(self, grid):
        ans=0
        maxans=0
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                stack=[]
                #print(maxans)
                if grid[i][j]==1:
                    stack.append([i,j])

                    while(stack):
                        #print(stack)
                        temp=stack.pop()
                        ans+=1
                        #print(ans)
                        grid[temp[0]][temp[1]]=0
                        #print(grid)
                        #←
                        if legal_location(temp[0]-1,temp[1],m,n) and grid[temp[0]-1][temp[1]]==1:
                            grid[temp[0]-1][temp[1]]=0
                            stack.append([temp[0]-1,temp[1]])
                        #→
                        if legal_location(temp[0]+1,temp[1],m,n) and grid[temp[0]+1][temp[1]]==1:
                            grid[temp[0]+1][temp[1]]=0
                            stack.append([temp[0]+1,temp[1]])
                        #↑
                        if legal_location(temp[0],temp[1]+1,m,n) and grid[temp[0]][temp[1]+1]==1:
                            grid[temp[0]][temp[1]+1]=0
                            stack.append([temp[0],temp[1]+1])
                        #↓
                        if legal_location(temp[0],temp[1]-1,m,n) and grid[temp[0]][temp[1]-1]==1:
                            grid[temp[0]][temp[1]-1]=0
                            stack.append([temp[0],temp[1]-1])
                    if ans>=maxans:
                        maxans=ans
                    ans=0
        return maxans