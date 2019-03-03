import collections
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if not A:return []
        check = A[0]
        numscheck = collections.Counter(check)
        for string in A:
            for temp in numscheck:
                if temp in string:
                    numscheck[temp] = min(numscheck[temp],string.count(temp))
                else:
                    numscheck[temp]=0
        res = []
        for temp in numscheck:
            for i in range(numscheck[temp]):
                res.append(temp)
        return res