import collections
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:return 1
        first = []
        second = []
        for tmp in trust:
            first.append(tmp[0])
            second.append(tmp[1])
        fir_check = collections.Counter(first)
        sec_check = collections.Counter(second)
        
        for u in sec_check:
            if sec_check[u] == N-1 and u not in fir_check:
                return u
        return -1