
'''
686. Repeated String Match
2017.12.22
'''
操作必然是有上界的
class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        x=1
        while x<=2*max(len(B)/len(A),1):
            if B in x*A:
                return x
            x+=1
        return -1