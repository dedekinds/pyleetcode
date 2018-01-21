'''
766. Toeplitz Matrix
2018.1.21
'''

循环矩阵，将待循环的部分取出来
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        if len(matrix)==1 or len(matrix[0])==1:
            return True
            
        matrix[-1][0]=matrix[0][-1]
        #print(matrix)
        m=len(matrix[0])
        n=len(matrix)
        

        temp=[]
        cnt=0
        check=matrix[0]
        for x in range(1,n-1):
            temp+=[matrix[x][0]]
        check=check+temp[::-1]

        last=(check[m-1:]+check[:m])
        #print(last)
        mat=matrix[::-1]
        for x in range(n):
            if mat[x] != last[x:x+m]:
                return False
        return True
        
                    

                
                
