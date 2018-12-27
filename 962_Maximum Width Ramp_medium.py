
将序号按照数组的大小进行排序，这样的话问题就会转换为，对于新的序号，找到最大的间隔
此时我们从左开始，不断保存最小值，并更新当前值和最小值的差（取最大的那个即可

class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        temp = zip(range(len(A)),A)
        temp = sorted(temp,key = lambda x:x[1])
        res = 0
        m = float('inf')
        for index,value in temp:
            res = max(res,index - m)
            m = min(index,m)
        return res
——————————————————————————————————————————————————————————————————————
