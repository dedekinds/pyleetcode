'''
290. Word Pattern
2018.1.22
'''
和同构字符串那题一样，构造单射满射即可
class Solution(object):
    def wordPattern(self, pattern, S):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=S.split()

        if len(pattern)*len(s)==0:
            return False
        if len(pattern) != len(s):
            return False
        temp=dict()
        for x in range(len(pattern)):
            check=temp.get(pattern[x],-1)
            if check != -1:
                if temp[pattern[x]] != s[x]:
                    return False
            else:
                if s[x] not in temp.values():
                    temp[pattern[x]]=s[x]
                else:
                    return False
        return True
            
        
        
