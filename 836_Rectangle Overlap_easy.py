class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        left = rec1[0] >= rec2[2]
        right = rec1[2] <= rec2[0]
        up = rec1[3] <= rec2[1]
        bottom = rec1[1] >= rec2[3]
        return not(left or right or up or bottom)