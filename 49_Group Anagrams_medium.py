class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for s in strs:
            tmp = tuple(sorted(s))
            d[tmp] = d.get(tmp,[]) + [s]
        return d.values()
        
        