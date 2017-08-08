'''34. Search for a Range 
   2017.8.8
'''
def leftbinsearch(nums,target):
    #二分查找找到第一个所需元素
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right)>>1
        if nums[mid]<target:
            left=mid+1#主要修改了这里
        else:
            right=mid
    return left
        
def rightbinsearch(nums,target):
    #二分查找找到最后一个所需元素
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right+1)>>1#和上面有一点点不同left+right+1
        if nums[mid]>target:
            right=mid-1
        else:
            left=mid
    return right

class Solution(object):
    def searchRange(self, nums, target):
        #处理特殊情况
        if len(nums)==0:
            return [-1,-1]
        if len(nums)==1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        #做一次二分判断是否存在
        ans=[]
        left=0
        right=len(nums)-1

        #下面是普通二分查找
        if nums[0]==target or nums[-1]==target:
            ans.append(leftbinsearch(nums,target))
            ans.append(rightbinsearch(nums,target))
            return ans
        while left+1!=right:
            mid=int(left+(right-left)/2)
            if nums[mid]<target:
                left=mid
            elif nums[mid]>target:
                right=mid
            else:
                ans.append(leftbinsearch(nums,target))
                ans.append(rightbinsearch(nums,target))
                return ans
        return [-1,-1]