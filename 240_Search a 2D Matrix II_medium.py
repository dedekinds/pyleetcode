'''
240. Search a 2D Matrix II
2018.3.2
'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if  len(matrix)==0 or len(matrix[0])==0:
            return False
        x=len(matrix)-1
        y=0
        while x>-1 and y<len(matrix[0]):
            #print(x,y)
            if matrix[x][y]>target:
                x-=1
                continue
            if matrix[x][y]<target:
                y+=1
                continue
            else:return True
        return False
        