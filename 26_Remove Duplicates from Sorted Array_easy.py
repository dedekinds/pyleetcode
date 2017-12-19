
'''
26. Remove Duplicates from Sorted Array
2017.12.19
'''
快慢指针来去除重复，好像一起碰到过这种算法
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        slow=0
        for fast in range(1,len(nums)):
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
            fast+=1
        return slow+1