'''
67. Add Binary
2017.12.26
'''
考虑一个很好懂得递归（语言式
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)==0:return b
        if len(b)==0:return a
        if a[-1]=='1' and b[-1]=='1':
            return self.addBinary(self.addBinary(a[:-1],b[:-1]),'1')+'0'
        if a[-1]=='0' and b[-1]=='0':
            return self.addBinary(a[:-1],b[:-1])+'0'
        else:
            return self.addBinary(a[:-1],b[:-1])+'1'
