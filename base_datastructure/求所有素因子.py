求所有素因子，O(logN)
def primeFactor(self,n):
    ans = []
    if n%2==0: 
        ans.append(2)
    while n%2==0:
        n = n//2
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            ans.append(i)
        while n%i==0:
            n = n//i
    if n > 2:#最后可能还有一个素数
        ans.append(n)
    return ans