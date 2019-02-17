层次遍历
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        Q = []
        one = []
        dirr = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    Q.append((i,j))
                if grid[i][j] == 1:
                    one.append((i,j))
        #print(Q)
        #print(one)
        cnt = 0
        m = len(grid)
        n = len(grid[0])
        while Q:
            tempQ = []
            check = False
            for tmp in Q:
                for dirc in dirr:
                    x = tmp[0] + dirc[0]
                    y = tmp[1] + dirc[1]
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == 1:
                            check = True
                            tempQ.append((x,y))
                            grid[x][y] = 2
                    
            if check:cnt += 1
            Q = tempQ
        #print(grid)
        for ones in one:
            x = ones[0]
            y = ones[1]
            if grid[x][y] == 1:
                return -1
        return cnt