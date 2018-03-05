'''
221. Maximal Square
2018.3.5
'''
class Solution: 
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #dp[x][y]表示以坐标(x, y)为右下角元素的全1正方形矩阵的最大长度（宽度）
        #dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        ans=0
        dp=[[0]*len(matrix[0]) for x in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[i][j]=int(matrix[i][j])
                ans=max(ans,dp[i][j])
                if i and j and matrix[i][j]=='1':
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    ans=max(ans,dp[i][j])
        return ans**2
        