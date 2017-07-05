'''63. Unique Paths II 
   2017.7.5

'''
可以和62题结合起来看，这个实际上就是分析动态规划复杂度的那个杨辉三角递推式
做一个动态规划就好了，一般情况直接上数学表达式
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:#首尾有障碍直接
            return 0
        
        for i in range(len(obstacleGrid)):#障碍变成0
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
                else:
                    obstacleGrid[i][j]=3
                    
        obstacleGrid[0][0]=1
        for i in range(1,len(obstacleGrid)):
            if obstacleGrid[i][0]!=0:
                obstacleGrid[i][0]=obstacleGrid[i-1][0]
        for j in range(1,len(obstacleGrid[0])):
            if obstacleGrid[0][j]!=0:
                obstacleGrid[0][j]=obstacleGrid[0][j-1]             
        for i in range(1,len(obstacleGrid)):#开始递推
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j]==0:
                    continue
                else:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
