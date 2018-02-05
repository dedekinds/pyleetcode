'''
451. Sort Characters By Frequency
2018.2.5
'''
import collections
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(nums*string for nums,string in collections.Counter(s).most_common())https://leetcode.com/submissions/detail/139463645/