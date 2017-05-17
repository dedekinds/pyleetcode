'''136 Single Number  
   2017.5.17
   162ms
   beats 1.50%
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #统计一个数组的元素出现次数，查一查
        temp=sorted(nums)
        temp.append('A')
        print(temp)
        for x in [y for y in range(len(nums)) if y%2==0]:
            if temp[x]!=temp[x+1]:
                return temp[x]

'''
best code
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums))*2-sum(nums)


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans