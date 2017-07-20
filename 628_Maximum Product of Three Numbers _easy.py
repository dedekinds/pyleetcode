'''628. Maximum Product of Three Numbers  
   2017.7.20

'''
直接排序，然后对比  最大的三个  和  最小的两个和最大的数之乘积  的大小
O(nlogn)居然通过了...
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        a=nums[0]*nums[1]*nums[-1]
        b=nums[-1]*nums[-2]*nums[-3]
        if a>=b:return a
        else:return b




————————————————————————————
数据不够长，应该用堆排序什么的才是最好的，下面的方法是维护一个
最大的三个数和最小的两个数，复杂度是O(n)
class Solution(object):
    def maximumProduct(self, nums):
        max1,max2,max3,min1,min2=-1003,-1002,-1001,1001,1002
        for num in nums:
            if num>=max1:
                max1,max2,max3=num,max1,max2
            elif num>=max2:
                max2,max3=num,max2
            elif num>max3:
                max3=num
            if num<=min1:
                min1,min2=num,min1
            elif num<min2:
                min2=num
        return max(max1*max2*max3,max1*min1*min2)