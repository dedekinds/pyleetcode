'''540. Single Element in a Sorted Array 
   2017.9.7
'''
用二分法，实际上可以将数组分为[left,mid][mid+1,right]或者[left,mid-1]
两部分，然后选择只有奇数长度的心数组进行同样的处理

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)>>1
            if nums[mid]==nums[mid-1]:
                if (mid-1)%2==1:
                    right=mid-2
                else:
                    left=mid+1
            elif nums[mid]==nums[mid+1]:
                if (mid+1)%2==1:
                    left=mid+2
                else:
                    right=mid-1
            else:
                return nums[mid]#和左右两边的都不等
        return nums[left]