'''476.Number Complement   
   2017.5.16
   45ms
   beats 48.5%
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
32ms
'''


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        return num ^ 2 ** (len(bin(num))-2) - 1

