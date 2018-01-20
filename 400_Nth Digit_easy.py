'''
400. Nth Digit
2018.1.20
'''
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        #2^32=4294967296
        #1-9
        #10-99
        #100-999
        #....
        #1000000000-999999999
        
        #确定区间
        check=[9*pow(10,x-1)*x  for x in range(0,10)]
        true_check=[]
        temp=0
        for x in check:
            temp+=x
            true_check.append(temp)
        
        
        for x in range(len(true_check)):
            if n<true_check[x]:
                n-=true_check[x-1]
                i=x#位数
                break
        
        l=int(n/i+0.5)#第几个数(上取整)
        k=int(n%i)
        temp=int(pow(10,i-1)+l-1)

        #print(l,k,temp)
        #print(n,k,i)
        #print(true_check)
        return int(str(temp)[k-1])
        
            