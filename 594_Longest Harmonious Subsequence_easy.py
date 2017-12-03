'''
594. Longest Harmonious Subsequence 
2017.12.3
'''
用collections.Counter哈希统计，然后key递增，然后O(n)寻找相邻小于等于1的key，
维护一个ans(max)
import collections
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=collections.Counter(nums)
        ans=0
        pointer=None
        pointer_val=0
        for key,val in sorted(temp.items()):
            if pointer is not None and pointer+1==key:
                ans=max(ans,val+pointer_val)
            pointer=key
            pointer_val=val
        return ans