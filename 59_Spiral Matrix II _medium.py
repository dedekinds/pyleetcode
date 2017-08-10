'''59. Spiral Matrix II 
   2017.8.10
'''

和54. Spiral Matrix 类似
 1 2 3 4               a a a a
 5 6 7 8       变成    a 6 7 a 
 9 10 11 12            a a a a
 构造边界

 
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==1:
            return [[1]]
        if n==0:
            return []
        
        matrix=[[0]*n for x in range(n)]
        i,j=0,0
        cnt=1
        #先处理外层
        temp=1
        if cnt==1:
            for x in range(n-1):
                matrix[i][j+x]=temp
                temp+=1
            j+=x+1
            cnt=2
        if cnt==2:
            for x in range(n-1):
                matrix[i+x][j]=temp
                temp+=1
            i+=x+1
            cnt=3
        if cnt==3:
            for x in range(n-1):
                matrix[i][j-x]=temp
                temp+=1
            j-=x+1
            cnt=4
        if cnt==4:
            for x in range(n-1):
                matrix[i-x][j]=temp
                temp+=1
            i-=x
            cnt=1
            
        #处理里面
        while temp<=n*n:
            #→
            if cnt==1:
                while True:
                    j+=1
                    matrix[i][j]=temp
                    temp+=1
                    if matrix[i][j+1]!=0:
                        break
                cnt=2
                continue
            
            #↓
            if cnt==2:
                while True:
                    i+=1
                    matrix[i][j]=temp
                    temp+=1
                    if matrix[i+1][j]!=0:
                        break
                cnt=3
                continue
            #←
            if cnt==3:
                while True:
                    j-=1
                    matrix[i][j]=temp
                    temp+=1
                    if matrix[i][j-1]!=0:
                        break 
                cnt=4
                continue
            #↑
            if cnt==4:
                while True:
                    i-=1
                    matrix[i][j]=temp
                    temp+=1
                    if matrix[i-1][j]!=0:
                        break
                cnt=1
                continue
        
        return matrix
        