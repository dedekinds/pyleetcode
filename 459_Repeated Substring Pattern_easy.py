
'''
459. Repeated Substring Pattern 
2017.12.15
'''
看自己的博客
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp=s*2
        return temp[1:-1].find(s)!=-1
        
        '''
        #O(n)
        for x in range(int(len(s)/2)):
            temp=s[0:(x+1)]
            times=int(len(s)/(x+1))
            if temp*times==s:
                return True
        return False      
        '''
