class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        empty = 0
        self.pathnum = 0
        init_x = 0
        init_y = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        for i,row in enumerate(grid):
            for j,val in enumerate(row):
                if val == 0:
                    empty += 1
                if val == 1:
                    init_x,init_y = i,j
                    
                    
        def dfs(i,j,cnt):
            if grid[i][j] == 2:
                if cnt == empty+1:
                    self.pathnum += 1
                return
            grid[i][j] = -1
            for dir in dirs:
                nexti = i + dir[0]
                nextj = j + dir[1]
                if 0 <= nexti <len(grid) and 0<= nextj <len(grid[0]) and grid[nexti][nextj] != -1:
                    dfs(nexti,nextj,cnt+1)
            grid[i][j] = 0
        
        
        
        
        dfs(init_x,init_y,0)
        return self.pathnum
        