'''7. Reverse Integer 
   2017.7.27

'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp=str(x)[::-1]
        if x>=0 and int(temp)<pow(2,31):
            return int(temp)
        elif x<0 and int((temp)[:-1])<pow(2,31):
            return -int((temp)[:-1])
        else:
            return 0