
'''
204. Count Primes
2017.12.26
'''
埃拉托色尼筛法

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        check=[True]*max(n,2)
        check[0]=False
        check[1]=False
        x=2
        
        while x*x<n:
            if check[x]:
                temp=x*x#在x后面第一个开始去掉的数就是x*x
                while temp<n:
                    check[temp]=False
                    temp+=x
            
            
            x+=1
        return sum(check)