'''
682. Baseball Game 
2017.11.2
'''
直接对每次的结果用栈来保存
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans=[0]
        for x in ops:
            if x=='C':
                ans.pop()
            elif x=='D':
                ans.append(ans[-1]+2*(ans[-1]-ans[-2]))
            elif x=='+':
                ans.append(ans[-1]+ans[-1]-ans[-2]+ans[-2]-ans[-3])
            else:
                ans.append(ans[-1]+int(x))
        return ans[-1]
            
        