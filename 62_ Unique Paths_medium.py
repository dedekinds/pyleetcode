'''62. Unique Paths
   2017.7.5

'''
纯数学做法，实际上是杨辉三角的解：
import math
class Solution(object):
    def uniquePaths(self, m, n):
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))


用递推式解杨辉三角：
class Solution(object):
    def uniquePaths(self, m, n):
        obstacleGrid=[[0]*n for x in range(m)]
        obstacleGrid[0][0]=1
        for i in range(1,len(obstacleGrid)):
            obstacleGrid[i][0]=obstacleGrid[i-1][0]
        for j in range(1,len(obstacleGrid[0])):
            obstacleGrid[0][j]=obstacleGrid[0][j-1]             
        for i in range(1,len(obstacleGrid)):#开始递推
            for j in range(1,len(obstacleGrid[0])):
                obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]


