'''
171. Excel Sheet Column Number 
2017.11.14
'''
26进制转10进制系列
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for temp in s:
            ans=ans*26+ord(temp)-ord('A')+1
        return ans