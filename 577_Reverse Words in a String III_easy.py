'''577.Reverse Words in a String III  
   2017.5.16
   152ms
   beats 18.2%
'''
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num^(pow(2,len(bin(num)[2:]))-1)

'''
The best code
42ms
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([word[::-1] for word in s.split(' ')])
