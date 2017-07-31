'''387. First Unique Character in a String 
   2017.7.31
'''
采用一个新技术，直接字母统计

import collections

class Solution(object):
    def firstUniqChar(self, s):
        ans=-1
        temp=collections.Counter(s)
        for x,c in enumerate(s):
            if temp[c]==1:
                ans=x
                break
        return ans