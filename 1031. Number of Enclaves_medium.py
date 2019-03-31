class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        stack = []
        for i in range(len(A)):
            if A[i][0] == 1 and (i,0) not in stack:
                stack.append((i,0))
            if A[i][-1] == 1 and (i,len(A[0])-1) not in stack:
                stack.append((i,len(A[0])-1))
        for j in range(len(A[0])):
            if A[0][j] == 1 and (0,j) not in stack:
                stack.append((0,j))
            if A[len(A)-1][j] == 1 and (len(A)-1,j) not in stack:
                stack.append((len(A)-1,j))
        while stack:
            temp = stack.pop()
            A[temp[0]][temp[1]] = 0
            for dirs in dir:
                x = temp[0] + dirs[0]
                y = temp[1] + dirs[1]
                if x>=0 and x< len(A) and y >=0 and y<len(A[0]) and A[x][y] == 1:
                    A[x][y] = 0
                    if (x,y) not in stack:
                        stack.append((x,y))
        return(sum(sum(A,[])))