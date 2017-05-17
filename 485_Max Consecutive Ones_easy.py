'''485 Max Consecutive Ones
   2017.5.17
   126ms
   beats 30.81%
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=''
        for x in nums:
            temp=temp+str(x)
        K=temp.split('0')
        return max([len(y) for y in K])

'''
best code
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        maxL = 0
        for d in nums:
            if d == 1:
                tmp += 1
            else: 
                if maxL <= tmp:
                    maxL = tmp
                tmp = 0
        if maxL <= tmp:
            maxL = tmp
        return maxL