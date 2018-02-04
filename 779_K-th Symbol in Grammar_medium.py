'''
779. K-th Symbol in Grammar
2018.2.4
'''
def temp(nums,zero_one):
    if nums%2==1:
        if zero_one==0:return 0#01
        if zero_one==1:return 1#10
    if nums%2==0:
        if zero_one==0:return 1#01
        if zero_one==1:return 0#10
        
class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N==1 and K==1:
            return 0
        if N==2 and K==1:return 0
        if N==2 and K==2:return 1
        
        return temp(K,self.kthGrammar(N-1,int((K+1)/2)))
        
        
        