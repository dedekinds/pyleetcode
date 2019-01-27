import collections
class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        check = collections.Counter()
        for i in range(len(A)):
            for j in range(len(A)):
                check[A[i]&A[j]] += 1
        for i in range(len(A)):
            for tmp in check:
                if A[i] & tmp == 0:
                    ans += check[tmp]
        return ans