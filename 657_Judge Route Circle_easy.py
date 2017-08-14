'''657. Judge Route Circle 
   2017.8.14
'''
代数和为0的思想 beat 100%
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        ud_ans=0
        lr_ans=0
        for x in moves:
            if x=='U':
                ud_ans+=1
                continue
            if x=='D':
                ud_ans-=1
                continue
            if x=='L':
                lr_ans+=1
                continue
            if x=='R':
                lr_ans-=1
                continue
        if ud_ans==0 and lr_ans==0:
            return True
        else:
            return False