import math
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if bound == 0:return []
            
        if x == 1:
            exp_x = 0
        else:
            exp_x = int(math.log(bound,x))
        if y == 1:
            exp_y = 0
        else:
            exp_y = int(math.log(bound,y))
            
        #print(exp_x,exp_y)
        ans = []
        for i in range(exp_x+1):
            for j in range(exp_y+1):
                tmp = x**i + y**j
                if tmp not in ans and tmp <= bound:
                    ans.append(x**i+y**j)
        return ans