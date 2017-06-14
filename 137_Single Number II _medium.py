'''137. Single Number II 
   2017.6.14
'''
class Solution(object):
    def singleNumber(self, nums):
        a = b = 0
        for n in nums:
            b = (b^n)&~a
            a = (a^n)&~b
        return b

如果不是3个数而是两个数的话，利用异或的可交换性可以直接不断异或得到

对于统计1~N的那种统计正整数来说：
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(len(nums)):#对于正整数计数有效，1~N的正整数计数
            if nums[x]>0:
                while True:
                    #print(nums)
                    if nums[nums[x]-1]==nums[x]:#!!!防止如[2,1,4,1,4,1,4]这样卡位
                        nums[x]=-1
                        break
                    if nums[nums[x]-1]>0:
                        temp=nums[nums[x]-1]
                        nums[nums[x]-1]=-1
                        nums[x]=temp
                    if nums[nums[x]-1]<=0:
                        nums[nums[x]-1]-=1
                        nums[x]=0
                        break
        for x in range(len(nums)):
            if nums[x]==-1:
                return x+1
        return nums