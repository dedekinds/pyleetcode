三个方向分别求，很容易找到规律
class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0 or len(grid[0])==0:
            return 0
        #top
        top_area = len(grid)*len(grid[0])
        side_area = 0
        front_area = 0
        for temp in grid:
            top_area -= temp.count(0)
            side_area += max(temp)
        for j in range(len(grid[0])):
            temp_max = -1
            for i in range(len(grid)):
                if grid[i][j] > temp_max:
                    temp_max = grid[i][j]
            front_area += temp_max
        return top_area + side_area + front_area
            
        
        
        
        