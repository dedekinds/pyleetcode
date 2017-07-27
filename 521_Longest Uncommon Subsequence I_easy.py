'''521. Longest Uncommon Subsequence I 
   2017.7.27

'''
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a==b:return -1
        else:return max(len(a),len(b))