'''179. Largest Number 
   2017.7.26

'''
给sort加特定排序的两个办法

from functools import cmp_to_key
def compare(a,b):
    return [1,-1][a+b>b+a]
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        temp = cmp_to_key(compare)
        res = ''.join(sorted([str(x) for x in nums], key=temp)).lstrip('0')
        if res=='':
            return '0'
        return res
    
    

    class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def comp(n1, n2):
            s1 = n1 + n2
            s2 = n2 + n1
            if s1 < s2: return -1
            elif s1 > s2: return 1
            else: return 0
        
        strnums = [str(x) for x in nums]
        strnums.sort(comp, reverse=True)
        ret = "".join(strnums)
        if ret[0] == ret[-1] == '0': return "0"
        else: return ret
