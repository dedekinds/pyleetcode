'''389. Find the Difference 
   2017.5.18
   39ms
   beats 73.83%
'''
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letter=[0]*26
        for c in s:
            letter[ord(c)-97]+=1
        for c in t:
            letter[ord(c)-97]-=1
            if letter[ord(c)-97]<0:
                return c



http://www.2cto.com/kf/201609/543954.html