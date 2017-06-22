'''1. Two Sum 
   2017.6.22
   169ms
'''

——————————错误的方法————————————
def binsearch(nums,target):
    if nums[0]==target:
        return 0
    if nums[-1]==target:
        return len(nums)-1
    left=0
    right=len(nums)-1
    while(left+1!=right):
        mid=int(left+(right-left)/2)#思路是先用爽指针夹逼出解，然后用二分搜出答案
        if nums[mid]>target:#但是要是如nums=[3,3],target=6的话，输出结果为[0,0]
            right=mid#其次似乎二分是需要排序的，如果是这样的话，那么对输出的序号是不利的，本方法是错误的
        if nums[mid]<target:
            left=mid
        if nums[mid]==target:
            return mid
    return -1

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp=sorted(nums)
        left=0
        right=len(nums)-1
        while (left<right):
            if temp[left]+temp[right]==target:
                a=binsearch(nums,temp[left])
                b=binsearch(nums,temp[right])
                return [a,b]
                break
            if temp[left]+temp[right]>target:
                right-=1
            if temp[left]+temp[right]<target:
                left+=1