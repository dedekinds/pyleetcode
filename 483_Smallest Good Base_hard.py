
'''483. Smallest Good Base 
   2017.6.12
   似乎用pow对大数会GG，本地测评都各种爆了，尽量用对数吧
'''
import math
def functiontemp(a,k):
    return (pow(a,k+1)-1)/(a-1)

def binsearch(tar,k):#精度版二分a,2<=a<=n-1
    eps=0.0001
    left=2
    right=tar-1
    if (functiontemp(left,k)-tar)**2<eps:
        return left
    if (functiontemp(right,k)-tar)**2<eps:
        return right
    while(left+1!=right):
        mid=int(left+(right-left)/2)
        #print(left,right,'k=',k,'mid=',mid)
        if (functiontemp(mid,k)-tar)**2<eps:
            return mid
        if functiontemp(mid,k)>tar:
            right=mid
        if functiontemp(mid,k)<tar:
            left=mid
    return -1


class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        #1+a+a2+a3+...ak=n
        #求约数
        dis=[]
        #傻逼了，遍历k才是坠吼的
        n=int(n)
        for k in range(1,1+int(math.log(n,2))):
            tar=n
            temp=binsearch(tar,k)
            if temp!=-1:
                dis.append(temp)
        if len(dis)==0:
            return str(n-1)#如果都不是，肯定是n-1            
        return str(min(dis))



'''483. Smallest Good Base 
   2017.6.12
   公约数求解时候是线性遍历的最终上O(Nln(lnN))，不应该对a遍历，对k遍历啊，取n对数2遍历
'''
import math
def binsearch(arr,tar):
    length=len(arr)
    eps=0.00001
    if (arr[0]-tar)**2<=eps:
        return 0
    if (arr[-1]-tar)**2<=eps:
        return length-1
    if length==1:#若首尾都没有所期望的值且长度为1那么return -1
        return -1
    left=0
    right=length-1
    #print(arr,tar)
    while (left+1 != right):
        #print(left,right)
        mid = int(left+(right-left)/2)
        if (arr[mid]-tar)**2<=eps:
            return mid
        if arr[mid]>tar:
            right=mid
        if arr[mid]<tar:
            left=mid
    return -1

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        dis=[]#存可能的情况a
        #求约数
        for a in range(2,1+int(math.sqrt(n))):
            tar=math.log(n*(a-1)+1,a)-1
            arr=list(range(1,1+int(math.log(n,a))))
            if (n-1)%a==0 and binsearch(arr,tar)!=-1:
                dis.append(a)
                
                a=int((n-1)/a)#考虑对应的另一个约数
                tar=math.log(n*(a-1)+1,a)-1
                arr=list(range(1,1+int(math.log(n,a))))
                if  binsearch(arr,tar)!=-1:
                    dis.append(a)
        if len(dis)==0:
            return n-1
        return min(dis)
    #若不行就输出n-1
                     
n=1000000000000000000
temp=Solution()
print(temp.smallestGoodBase(n))
#print(binsearch(nums,target))

