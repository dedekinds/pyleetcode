s神操作，考虑头部或者不考虑，然后组合起来，可以一同参考combinations这题

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        subset = self.subsets(nums[1:])
        ans = subset + [[nums[0]] + tmp for tmp in subset]
        return ans