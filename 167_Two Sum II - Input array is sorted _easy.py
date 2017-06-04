'''167. Two Sum II - Input array is sorted 
   2017.6.4

'''
#双二分查询
def binsearch(arr,tar):
    length=len(arr)
    if arr[0]==tar:
        return 0
    if arr[-1]==tar:#两个边界干脆特殊处理好了
        return (length-1)
    left=0
    right=length-1
        
    while (left+1 != right):#用这个可以在不存在时，避免死循环
        mid = int(left+(right-left)/2)#二分查找
        if arr[mid]>tar:
            right=mid
        if arr[mid]<tar:
            left=mid
        if arr[mid]==tar:
            return mid
    return -1
class Solution(object): 
    def twoSum(self, numbers, target):
        A=sorted(list(set(numbers)))
        #先去掉重复，前后双二分查询，最后输出的序号排序即可？
        #注意到有且仅有两个数之和，这种方法可能行
        for x in range(len(A)):
            ans1=binsearch(numbers,A[x])
            ans2=binsearch(numbers,target-A[x])
            if ans1==ans2:
                if numbers[ans1]==numbers[ans1+1]:#对于WA1的处理
                    return [ans1+1,ans1+2]
                else:
                    return [ans1,ans1+1]
            if ans2!=-1:
                return sorted([ans1+1,ans2+1])

__#跌跤提供的O(n)方法___________________________________
class Solution(object): 
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1
        while (left<right):
            if numbers[left]+numbers[right]>target:
                right-=1
            if numbers[left]+numbers[right]<target:
                left+=1
            if numbers[left]+numbers[right]==target:
                return [left+1,right+1]

就是它是已经排序好的嘛，那么你从两端开始加起来，和目标值进行比较，
如果比目标值大，说明应该放小一点，这时候左端已经是最小了，没得再放，
那就把右端（假设是b）放小，即算b-1处和左端的和








——————————下面这种办法O(nlogn)超时
from numpy import *
def binsearch(arr,tar):
    length=len(arr)
    if arr[0]==tar:
        return 0
    if arr[-1]==tar:#两个边界干脆特殊处理好了
        return (length-1)
    left=0
    right=length-1
        
    while (left+1 != right):#用这个可以在不存在时，避免死循环
        mid = int(left+(right-left)/2)#二分查找
        if arr[mid]>tar:
            right=mid
        if arr[mid]<tar:
            left=mid
        if arr[mid]==tar:
            return mid
    return -1
class Solution(object): 
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #遍历找住一个，剩下的应该用二分查找的有可能O(NlogN)      
        for x in range(len(numbers)):
            temp=numbers[(x+1):]#取下一个到末尾进行二分查找
            ans2=binsearch(temp,(target-numbers[x]))
            if ans2!=-1:
                return [(x+1),(ans2+1)+(x+1)]#(x+1)是因为截掉了一部分


#TLE2:
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,...]
#5





——————————下面这种办法O(n^2)超时
from numpy import *
class Solution(object):
    
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(numbers)):
            numbers.append(target-numbers[x])
            tempindex=numbers.index(target-numbers[x])
            #在最后面append一个目标，这样的话就防止index报错
            #利用index的特性，如果有重复的话就返回第一个
            if tempindex!=(len(numbers)-1):
                if (x+1)<(tempindex+1):
                    return [x+1,tempindex+1]#针对WA1修改
                if (x+1)>(tempindex+1):
                    return [tempindex+1,x+1]
            else:
                numbers.pop()

           
numbers=[2, 7, 11, 15]
target=18
temp=Solution()
print(temp.twoSum(numbers,target))
#WA1:
#[0,0,3,4]
#0
#output:[1,2]


#TLE1:
#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,...]
#5












class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) <= 1:
            return False
        buff_dict = {}
        for i in range(len(numbers)):
            if numbers[i] in buff_dict:
                return [buff_dict[numbers[i]]+1, i+1]
            else:
                buff_dict[target - numbers[i]] = i