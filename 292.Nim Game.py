'''292.Nim Game   
   2017.5.19
   39ms
   beats 62.91%
'''
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%4==0:
            return False
        else:
            return True