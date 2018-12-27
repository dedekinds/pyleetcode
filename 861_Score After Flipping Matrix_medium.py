纯贪心了一下，首先看第一列1的个数是否超过一半，如果超过了，那么就不管，否则就对第0行进行一个操作
然后用行操作将第0列全部变为1，然后后面呢就怼不超过一半1的列做操作

但是为什么能成功呢？2^n > 2^ n−1+2^ n−2+⋯+2^0


class Solution:
    def get_col(self,A,col):
        check_col_sum = 0
        n = len(A)
        for i in range(n):
            check_col_sum += A[i][col]
        return check_col_sum >= (n+1)/2
    def change_col(self,A,col):
        n = len(A)
        for i in range(n):
            A[i][col] = 1 - A[i][col]
            
    def change_row(self,A,row):
        for i in range(len(A[row])):
            A[row][i] = 1 - A[row][i]
    def count_matrix(self,A):
        s = 0
        row = len(A)
        col = len(A[0])
#        for i in range(row):
#            for j in range(col):
#                s += 2**(col - j - 1)*A[i][j]             
        for j in range(col):
            power = 2**(col - j -1)
            for i in range(row):
                s += power*A[i][j]
        return s
        
        
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A)==0 or len(A[0])==0:return 0
        num_col = len(A[0])
        num_row = len(A)
        if not self.get_col(A,0):
            self.change_col(A,0)
        for temp in range(num_row):
            if A[temp][0] == 0:
                self.change_row(A,temp)
        
        for j in range(1,num_col):
            if not self.get_col(A,j):
                self.change_col(A,j)
        return self.count_matrix(A)


