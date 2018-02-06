'''
481. Magical String
2018.2.6
'''
class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        string='122'
        temp=2

        while len(string)<n:
            string+=int(string[temp])*str(3-int(string[-1]))
            temp+=1
        return string[:n].count('1')
