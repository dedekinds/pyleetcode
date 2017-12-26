'''
438. Find All Anagrams in a String
2017.12.26
'''
最下面写的是一个暴力O(mn)的算法，下面的这个是O(n)的算法

import collections
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        res = []
        left = right = 0
        count = len(p)
        dic = collections.Counter(p)
        
        while right < len(s):
            if s[right] in dic.keys():
                if dic[s[right]]>=1:
                    count = count - 1
                dic[s[right]] = dic[s[right]]-1
            right = right+1
            
            if count == 0 :
                res.append(left)
                
            if right - left == len(p):
                if s[left] in dic.keys():
                    if dic[s[left]]>=0:
                        count = count + 1
                    dic[s[left]]+=1
                left = left+1
        return res      
        
        '''
        check=collections.Counter(p)
        t=0
        len1=len(s)
        len2=len(p)
        ans=[]
        while t <= len1-len2:
            temp=collections.Counter(s[t:(t+len2)])
            if temp == check:
              #  print(temp)
                ans.append(t)
            t+=1
        return ans
                    
        '''
