
'''
434. Number of Segments in a String
2017.12.17
'''
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
        