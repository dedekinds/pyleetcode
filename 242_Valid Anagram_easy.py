'''242. Valid Anagram 
   2017.5.29
   516ms
   beats 0.76%
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        elif s==''and t=='':
            return True
            #针对空集情况
        tempA=[0]*26
        tempB=[0]*26
        #计算字母数量
        A=set(s)
        for x in A:
            for y in range(len(s)):
                if s[y]==x:
                    tempA[ord(x)-97]+=1
        B=set(t)
        for x in B:
            for y in range(len(t)):
                if t[y]==x:
                    tempB[ord(x)-97]+=1
                    
        for z in range(26):
            if tempA[z]!=tempB[z]:
                return False
        #print(tempA)
        #print(tempB)
        return True

'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for c in set(list(s)):  # do not forget preprocessing!
            if s.count(c) != t.count(c):
                return False
        return True