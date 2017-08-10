'''390. Elimination Game  
   2017.8.9
'''
class Solution(object):
    def lastRemaining(self, n):
        ans=1
        p=1
        temp=1
        while n>1:
            n=int(n/2)
            p*=2
            if temp==1:
                ans+=p/2+(n-1)*p
                temp=0
                continue
            if temp==0:
                ans-=p/2+(n-1)*p
                temp=1
                continue
        return ans
#目的是找到一个幸存者（没有被干掉的数）
'''
初始p=1,ans=1,n=n
p*=2
n=int(n/2)

第一种操作：
a+(n-1)p一定会被干掉，然后a+(n-1)p+p/2一定不会被干掉（注意这里的p/2，
另一方面a+(n-1)p+p/2没有越界，因为a+(n-1)p+p/2<=a+np

第二种操作：
a-[(n-1)p]一定会被干掉，然后a-(n-1)p-p/2一定不会被干掉，且没有越界
'''
——————————————————————————
对大数TLE，直接数组模拟 TLE
def firstdo(nums):
    nums.pop(0)
    return nums[::2]
def afterdo(nums):
    if len(nums)%2==0:
        return nums[::2]
    else:
        return firstdo(nums)
    
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=list(range(1,n+1))
        temp=1
        while len(nums)>1:
            if temp==1:
                nums=firstdo(nums)
                temp=0
                continue
            if temp==0:
                nums=afterdo(nums)
                temp=1
                continue
        return nums[0]

——————————————————————————————
递归大佬
class Solution(object):
    def lastRemaining(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
        return 2*(1+n/2-self.lastRemaining(n/2)) 