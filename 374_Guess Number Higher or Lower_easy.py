'''374. Guess Number Higher or Lower 
   2017.8.2
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
class Solution(object):
    def guessNumber(self, n):
        left=1
        right=n
        while left<=right:
            mid=(left+right)>>1
            temp=guess(mid)
            if temp==-1:
                right=mid-1
            elif temp==1:
                left=mid+1
            elif temp==0:
                return mid

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) >> 1
            trial = guess(mid)
            if trial == -1:
                right = mid - 1
            elif trial == 1:
                left = mid + 1
            else:
                return mid

'''
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
'''