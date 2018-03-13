'''
334. Increasing Triplet Subsequence
2018.3.13
'''
让a为当前最小
b为最近的比a大的数
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a, b = None,None
        for x in nums:
            if a is None or a>=x:
                a = x
            elif b is None or b>=x:
                b = x
            else:
                return True
        return False