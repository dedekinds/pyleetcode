'''
771. Jewels and Stones
2018.1.31
'''
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(x in J for x in S)
        