'''151. Reverse Words in a String 
   2017.7.26

'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp=s.split()
        temp.reverse()
        return ' '.join(temp)