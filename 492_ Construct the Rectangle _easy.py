'''492. Construct the Rectangle 
   2017.6.11
   59ms
'''
import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        #目前的想法是找一个a>=sqrt(area)且能整除area的数作为a即可
        #由于a更大遍历a是愚蠢的行为，不如遍历b
        for x in list(range(1,int(math.sqrt(area))+1))[::-1]:
            if area%x==0 and x<=math.sqrt(area):
                b=x
                a=int(area/b)
                return [a,b]
______________________________________

import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        #目前的想法是找一个a>=sqrt(area)且能整除area的数作为a即可
        for x in range(int(math.sqrt(area)),area+1):
            if area%x==0 and x>=math.sqrt(area):
                a=x
                b=int(area/a)
                return [a,b]

#area=9999992 TLE

