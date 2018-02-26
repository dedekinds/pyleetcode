'''
790. Domino and Tromino Tiling
2018.2.26
'''
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        2*n的棋盘被1*2的矩形块和1*1*1的L型块填满的方案总数
        f[0]=1
        f[1]=1
        f[2]=2
        f[n]=f[n-1]+f[n-2]+3\sum_{0}^{n-3}f[n] % 1000000007
        """
        
        #37ms
        f=[1]*(N+2)#如果是N+1的话呢，在N=1的时候，下面这个语句f[2]=2就无法执行了，所以干脆加多一位
        f[2]=2
        if N<3:return f[N]
        tempsum=f[0]+f[1]+f[2]
        for i in range(3,N+1):
            f[i]=(2*tempsum-f[i-1]-f[i-2])% 1000000007
            tempsum+=f[i]
        return f[N]

        #___________________________________________________
        #233ms
        f=[1]*(N+2)#如果是N+1的话呢，在N=1的时候，下面这个语句f[2]=2就无法执行了，所以干脆加多一位
        f[2]=2
        if N<3:return f[N]
        for i in range(3,N+1):
            f[i]=f[i-1]+f[i-2]+2*sum(f[0:(i-3+1)])
        return f[N]% 1000000007
        
        
