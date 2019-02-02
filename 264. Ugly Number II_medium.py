class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglynum = [1]
        if n <= 0:
            return 0
        index2 = 0
        index3 = 0
        index5 = 0
        for i in range(n-1):
            nextugly = min(uglynum[index2]*2,uglynum[index3]*3,uglynum[index5]*5)
            uglynum.append(nextugly)
            if nextugly % 2 == 0:index2 += 1
            if nextugly % 3 == 0:index3 += 1
            if nextugly % 5 == 0:index5 += 1
        #print(uglynum)
        return uglynum[-1]