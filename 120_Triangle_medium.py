
从底部开始反推，DP的方法
用minpath[k][i]表示以triangle[k][i]为头结点，最小的路径和，
那么最底端的就是自己本身了，然后
minpath[k][i] = min(minpath[k+1][i],minpath[k+1][i+1])+triangle[k][i]


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
        tall = len(triangle)
        width = len(triangle[-1])
        minpath = triangle[-1]
        
        index = list(range(tall-1))[::-1]
        for k in index:
            for i in range(len(triangle[k])):
                minpath[i] = min(minpath[i],minpath[i+1])+triangle[k][i]
        #print(minpath)
        return minpath[0]
        