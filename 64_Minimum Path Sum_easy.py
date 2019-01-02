class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0])==0:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(1,n):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        for j in range(1,m):
            grid[j][0] += grid[j-1][0]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = min(grid[i-1][j]+grid[i][j],grid[i][j-1]+grid[i][j])
        return grid[-1][-1]