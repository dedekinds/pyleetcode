class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = dict()
        for index,num in enumerate(nums):
            if target - num in idx:
                return [idx[target-num],index]
            idx[num] = index
————————————————————————————————————————————————————————————


'''1. Two Sum 
   2017.6.22
   169ms
'''

def findvalue(nums,target):#用双指针夹逼法获得我们要的数值
    temp=sorted(nums)
    left=0
    right=len(nums)-1
    while left<right:
        if temp[left]+temp[right]==target:
            return [temp[left],temp[right]]
        if temp[left]+temp[right]>target:
            right-=1
        if temp[left]+temp[right]<target:
            left+=1
class Solution(object):
    def twoSum(self, nums, target):#从左到右遍历一次，一共是O(n)
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        a,b=findvalue(nums,target)
        for x in range(len(nums)):
            if nums[x]==a:
                ans.append(x)
                nums[x]='temp'
            if nums[x]==b:
                ans.append(x)
                nums[x]='temp'
        return ans




——————————best 方法————————————
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)#哈希大法
        diff_dict ={}
        i = 0
        while i < n:
            if nums[i] not in diff_dict:
                diff_dict[target - nums[i]] = i #有点很巧妙
                i+=1
            else:
                return diff_dict[nums[i]], i


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