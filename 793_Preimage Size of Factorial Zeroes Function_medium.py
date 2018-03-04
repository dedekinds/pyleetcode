'''
793. Preimage Size of Factorial Zeroes Function
2018.3.4
'''
'''
0.f(x)=sum(int(n/5^i))

1.结果要么是0要么是5：sum(int(n/5^i))<=sum(n/5^i)
注意到sum(1/5^i)=1/4
所以如果f(n)=K,那么n n+1 n+2 n+3 n+4也同样成立

3.对N做一个二分，只要找到一个解就输出5，否则0，对left做个估算，sum(n/5^i)=>K>=sum(n/5^i)-log_5n，那么干脆取左边有n至少为4K，上界不严谨，
我这里随便给了一个0xffffffff，其实下界选1也没问题

'''
class Solution(object):
    def legren(self,n):
        k=1
        ans=0
        while n>1:
            ans+=int(n/5)
            n/=5
        return ans
            
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K==0:return 5
        left=4*K
        right=0xffffffff
        while left<=right:
            mid=(left+right)>>1
            if self.legren(mid)<K:
                left=mid+1
            elif self.legren(mid)>K:
                right=mid-1
            else:
                return 5
        return 0
        
        
        