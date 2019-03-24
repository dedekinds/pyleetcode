
a_n = 10^n + 10^(n-1) +...+1
由欧拉定理，若a和n互质，10^φ(n)=1 mod n，而a_0 = 1 mod n说明至少 φ(n)次就已经余数循环了
这说明至少遍历了一次剩余类，而剩余类的和一定能整除n，所以 min(n) <= φ(n)
更进一步的由于 φ(x)=x(1-1/p(1))(1-1/p(2))(1-1/p(3))(1-1/p(4))…..(1-1/p(n)) 其中p(1),p(2)…p(n)为x
的所有质因数，所以
min(n) <= φ(K) <K
所以只需要检查到K即可，不用再继续了


class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K%2==0 or K%5==0:return -1
        if K ==1:return 1
        r = 0
        for i in range(1,K+1):
            r = (r*10+1)%K
            if not r:return i
            
            