'''
58. Length of Last Word 
2017.10.15
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.split())==0:
            return 0
        return len(s.split()[-1])
