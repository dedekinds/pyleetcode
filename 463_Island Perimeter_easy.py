'''463 Island Perimeter   
   2017.5.17
   1479ms
   beats 0.19%
'''
from numpy import *
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        Perimeter=0
        for y in range(len(grid)):
            for x in range(int(size(grid)/len(grid))):#注意 x和y表示纵横呐
                if grid[y][x]==1:
                    Perimeter+=4
                    if x>0 and (grid[y][x-1]==1):
                        Perimeter=Perimeter-2
                    if y>0 and (grid[y-1][x]==1):#要用'and'不能用&啊
                        Perimeter=Perimeter-2 
        return Perimeter
'''
best code

'''
def islandPerimeter(self, grid):
    return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))