http://www.cnblogs.com/ZhangJinkun/p/4531395.html
https://blog.csdn.net/immiao/article/details/16909125
A在前面的数量总大于B排在前面的数量，且A和B的人数相同类型卡塔兰数

left达到N就结束了，后面填充)就可以了
否则呢，right的个数(即')')不能超过'('的个数left，否则就非法了

class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans