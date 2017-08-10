'''54. Spiral Matrix 
   2017.8.10
'''
 1 2 3 4               a a a a
 5 6 7 8       变成    a 6 7 a 
 9 10 11 12            a a a a
 构造边界

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m=len(matrix)
        ans=[]
        
        #处理空集
        if m==0:
            return ans
        n=len(matrix[0])
        
        #处理只有一层的情况：

        if m==1 or n==1:
            return sum(matrix,[])


        i,j=0,0
        cnt=1
        
        #先处理一次外层:
        if cnt==1:
            for x in range(n-1):
                ans.append(matrix[i][j+x])
                matrix[i][j+x]='dede'
            j+=x+1
            cnt=2
        if cnt==2:
            for x in range(m-1):
                ans.append(matrix[i+x][j])
                matrix[i+x][j]='dede'
            i+=x+1
            cnt=3
        if cnt==3:
            for x in range(n-1):
                ans.append(matrix[i][j-x])
                matrix[i][j-x]='dede'
            j-=x+1
            cnt=4
        if cnt==4:
            for x in range(m-1):
                ans.append(matrix[i-x][j])
                matrix[i-x][j]='dede'
            i-=x
            cnt=1

            
        while len(ans)<m*n:
            #→
            if cnt==1:
                while True:
                    j+=1
                    ans.append(matrix[i][j])
                    if matrix[i][j+1]=='dede':
                        break
                    matrix[i][j]='dede'
                cnt=2
                continue
            
            #↓
            if cnt==2:
                while True:
                    i+=1
                    ans.append(matrix[i][j])
                    if matrix[i+1][j]=='dede':
                        break
                    matrix[i][j]='dede'  
                cnt=3
                continue
            #←
            if cnt==3:
                while True:
                    j-=1
                    ans.append(matrix[i][j])
                    if matrix[i][j-1]=='dede':
                        break
                    matrix[i][j]='dede'  
                cnt=4
                continue
            #↑
            if cnt==4:
                while True:
                    i-=1
                    ans.append(matrix[i][j])
                    if matrix[i-1][j]=='dede':
                        break
                    matrix[i][j]='dede'
                cnt=1
                continue
            
        return ans


————————best___________
class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res