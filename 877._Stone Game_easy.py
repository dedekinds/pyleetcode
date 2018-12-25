原理是采用DP的方法，设d[i,j]表示的是对于A的index=i和index=j的两种序号下即A[i-j]的两者的差，
因为这是博弈问题，每次A选择最优操作，B也会选择最优操作的
于是就有下的递推式
class Solution:
    def stoneGame(self, A):
        """
        :type piles: List[int]
        :rtype: bool
        """
        if len(A) <=2:return True
        n = len(A)
        check = [[0]*len(A) for i in range(len(A))]
        for i in range(n):
            check[i][i] = A[i]
            if i < n -1:
                check[i][i+1] = abs(A[i] - A[i+1])
        for i in range(2,n):
            for j in range(i,n):
                check[j-i][j] = max(A[j-i]-check[j-i+1][j],A[j]-check[j-i][j-1])
        return check[0][n-1]>0
——————————————————————————————————————————————————————————————


这里我么将内存的消耗稍微减少一点，变成一维的
实际上就是，不断在原来的数组上更新即可
class Solution:
    def stoneGame(self, A):
        """
        :type piles: List[int]
        :rtype: bool
        """

        if len(A) <= 2:return True
        n = len(A)
        check = [0]*n
        for i in range(n):
            check[i] = A[i]
        for t in range(1,n):
            for i in range(n-t):
                check[i] = max(A[i] - check[i+1], A[i+d]-check[i])
        return check[0]>0
    
