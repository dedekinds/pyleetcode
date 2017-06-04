'''167. Two Sum II - Input array is sorted 
   2017.6.4

'''












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
