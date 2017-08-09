'''532. K-diff Pairs in an Array 
   2017.8.9
'''
暴力hash

import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<0:
            return 0
        c = collections.Counter(nums)
        ans=0
        if k==0:
            for n in c.keys():
                if c[n]>1:
                    ans+=1
        else:
            for n in c.keys():
                if c[n+k]>0:
                    ans+=1#c[i]不存在的话是0
        return ans
——————————————————————————
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        c = collections.Counter(nums)
        return sum(c[n + k] > 1 - bool(k) for n in c.keys())