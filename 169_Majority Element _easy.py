'''169. Majority Element 
   2017.5.27
   58ms
   beats 84.76%
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #————————————————————————————————
        #for x in nums:
        #    if nums.count(x)>=int(len(nums)/2)+1:
        #        return x
                #这种暴力算法对于很长的数组会TLE
                
        #————————————————————————————————
        A=set(nums)
        for x in list(A):
            if nums.count(x)>=int(len(nums)/2)+1:
                return x
#——————————
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]#确实由于长度大于一半，所以中间的个数必然就是我们要的数
#————————————————

似乎官方的想法是这个
思路：
http://blog.csdn.net/luoyingmin/article/details/52502871

此题要求选出一个数组中出现次数最多的那一个数，可用分治算法的思想，
将整个数组分成两个部分，先分别筛选出这两部分中出现次数最多的数，记为x和y，如果x等于y，
则返回x，如果x不等于y，则x和y都是最终结果的候选，此时需要遍历整个链表考察x和y出现的次数，
出现次数较多的就是最终返回的结果。复杂度T(n) = 2T(n/2) + O(n)，所以T(n) = O(nlogn)。