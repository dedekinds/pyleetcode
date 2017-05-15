'''561. Array Partition I 
   2017.5.14
   135ms
   beats 67.92%
'''
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=sorted(nums)
        return sum(temp[::2])

'''
The best code
'''
class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])