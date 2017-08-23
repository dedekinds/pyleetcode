'''205. Isomorphic Strings 
   2017.8.23
'''
既然是同构映射，那么就是双射了
我们首先遍历s如果不存在s→t，那么取当前的t为像
注意到仅仅这样是不行的，比如
s='paper'
t='titll'
因为是双射，所以，我们不能让两个元映射到同一个元上（单射

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        iso=dict()
        for x in range(len(s)):
            temp=iso.get(s[x],-1)
            if temp !=-1:
                if iso[s[x]] != t[x]:#保证满射
                    return False
            else:
                if t[x] not in iso.values():#保证单射
                    iso[s[x]]=t[x]
                else:
                    return False
        return True