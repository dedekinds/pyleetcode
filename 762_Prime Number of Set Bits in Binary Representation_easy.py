
'''
762. Prime Number of Set Bits in Binary Representation
2018.1.19
'''
#因为要大量重复判断素数，所以应该把素数表构造出来

    
class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        #构建素数表（埃拉托色尼筛法）
        length=100
        '''
    说好的↓呢
    L, R will be integers L <= R in the range [1, 10^6].
    R - L will be at most 10000.

        '''
        primejudge=[1]*(length+1)
        primejudge[0]=primejudge[1]=0
        
        for x in range(2,length+1):
            if primejudge[x]==1:
                temp=x*x
                while temp<=length:
                    primejudge[temp]=0
                    temp+=x
            
        
        #print(primejudge)
        ans=0
        for x in range(L,R+1):
            ans+=primejudge[bin(x).count('1')]
        return ans